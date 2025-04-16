#!/bin/bash
#copy fhirportal json 至 /home/ycyeh2/json/
sudo docker cp skhfhirportal:/server/media/json/ /home/ycyeh2/
# 步驟 1
cd /home/ycyeh2/cbiapi
# 步驟 2
python3 f2_cbioportal_preprocess_debug0201.py
# 步驟 3
cd /home/ycyeh2/cbioportal-docker-compose/
# 步驟 4
sudo docker-compose run cbioportal metaImport.py -u http://cbioportal:8080 -s study/data_upload/ -o
# 步驟 5
sudo docker-compose restart cbioportal
#清除停止中container
yes | sudo docker container prune
#sudo docker rm $(sudo docker ps -a -q)
