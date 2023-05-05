#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo mkdir -p /data/web_static/releases/test/ 
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
