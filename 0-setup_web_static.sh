#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

# Check if Nginx in installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install nginx -y
    sudo service nginx start
fi

# Checks if directory path exist and creates 
if [ ! -d "/data/" ];
then
    sudo mkdir "/data/"
fi

if [ ! -d "/data/web_static/" ];
then
    sudo mkdir "/data/web_static/"
fi

if [ ! -d "data/web_static/current" ];
then
    sudo mkdir "data/web_static/current"
fi

if [ ! -d "/data/web_static/releases" ];
then
    sudo mkdir "/data/web_static/releases/"
fi

if [ ! -d "/data/web_static/shared/" ];
then
    sudo mkidr "/data/web_static/shared"
fi

if [ ! -d "/data/web_static/releases/test" ];
then
    sudo mkdir "/data/web_static/releases/test"
fi

if [ ! -f "/data/web_static/releases/test/index.html" ];
then
    sudo touch "/data/web_static/releases/test/index.html"
fi

SOURCE_DIR = "/data/web_static/current"
TARGET_DIR = "/data/web_static/releases/test/"

# Remove existing symbolic link if it exists
if [ -L "$SOURCE_DIR" ]; then
  sudo rm "$SOURCE_DIR"
fi

# Creates a new link
sudo ln -s "$TARGET_DIR" "$SOURCE_DIR"

# Give ownership  to ubuntu user
sudo chown -R $USER:$USER /data/
sudo chown -R 755 /data/






