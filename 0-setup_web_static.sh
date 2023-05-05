#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/ 
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
echo "
server{
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html index.htm;

        location /hbnb_static{
                alias /data/web_static/current;
                index index.html index.htm;
        }

        location /redirect_me{
                return 301 https://github.com/vinnywalker96;
        }

        error_page 404 /404.html;
        location = /404.hmtl{
                internal;
        }
}"| sudo tee  /etc/nginx/sites-available/default > /dev/null
sudo service nginx restart
