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
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/
cat > /data/web_static/releases/test/index.html <<'EOF'
<html>
    <head>
    </head>
    <body>
         Holberton School
    </body>
</html>
EOF

SOURCE_DIR="/data/web_static/current"
TARGET_DIR="/data/web_static/releases/test/"

# Remove existing symbolic link if it exists
if [ -L "$SOURCE_DIR" ]; then
  sudo rm "$SOURCE_DIR"
fi

# Creates a new link
sudo ln -s "$TARGET_DIR" "$SOURCE_DIR"

# Give ownership  to ubuntu user
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
