#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(current_time)
        folder_name = "versions"
        local("mkdir -p {}".format(folder_name))
        local("tar -cvzf {}/{} web_static".format(folder_name,
                file_name))
        return "web_static packed: {}/{}".format(folder_name, file_name)
    except:
        return None
