#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null
then
   sudo apt-get update
   sudo apt-get -y nginx
fi
sudo mkdir -p /data/ 
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo service nginx restart
