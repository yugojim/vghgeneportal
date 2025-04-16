from django.contrib import admin
from .models import Permission,Genedata,Genepermission,Metaxlsx,Userright,Genezip
from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display = ('username', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login','date_joined')

@admin.register(Genepermission)
class GenepermissionAdmin(admin.ModelAdmin):
    #list display
    list_display = ['user', 'pmi', 'specimen', 'biomarker', 'rearrangements','GenomicFindings','VariantProperties','Trials','reportProperties','copy_number_alterations','short_variants']
    #list Filter
    list_filter = ('user','dateTimeOfUpload')
    # search list
    #search_fields = ['User']

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    #list display
    list_display = ['user', 'gene', 'patient', 'emergency', 'outpatient', 'inpatient', 'medication', 'report', 'administrative', 'up']
    #list Filter
    list_filter = ('user','dateTimeOfUpload')
    # search list
    #search_fields = ['User']

@admin.register(Genedata)
class GenedataAdmin(admin.ModelAdmin):
    #list display
    list_display = ['inlineRadioOptions', 'fileTitle', 'uploadedFile','status']
    #list Filter
    list_filter = ('fileTitle','dateTimeOfUpload')
    # search list
    #search_fields = ['User']

@admin.register(Metaxlsx)
class MetaxlsxAdmin(admin.ModelAdmin):
    #list display
    list_display = ['fileTitle', 'uploadedFile', 'dateTimeOfUpload','status']
    #list Filter
    list_filter = ('fileTitle','dateTimeOfUpload')
    # search list
    #search_fields = ['User']
    
@admin.register(Genezip)
class GenezipAdmin(admin.ModelAdmin):
    #list display
    list_display = ['fileTitle', 'uploadedFile', 'dateTimeOfUpload','status']
    #list Filter
    list_filter = ('fileTitle','dateTimeOfUpload')
    # search list
    #search_fields = ['User']

@admin.register(Userright)
class UserrightAdmin(admin.ModelAdmin):
    #list display
    list_display = ['fileTitle', 'uploadedFile', 'dateTimeOfUpload','status']
    #list Filter
    list_filter = ('fileTitle','dateTimeOfUpload')
    # search list
    #search_fields = ['User']

#admin.site.register(fhirip)
