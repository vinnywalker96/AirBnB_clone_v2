#!/usr/bin/python3
from fabric.api import put 
from fabric.api import env
from fabric.api import run
from fabric.api import sudo
from datetime import datetime
import os

env.hosts = ['54.144.46.42', '100.25.194.141']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Generates a .tgz archive from the contents of the webstatic
    """
    try:
        if not os.path.exists("versions"):
            os,mkdir("versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(current_time)
        local("tar -czvf {} web_static".format(filename))
        return filename
    except:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive file to the web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path)
        foldername = "/data/web_static/releases/" + os.path.splittext(filename)[0]
        run("mkdir -p {}".format(foldername))
        run("tar -xzf /tmp/{} -C {} -- strip-components=1".format(filename, foldername))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}".format(foldername))
        run("rm -rf {}/web_static".format(foldername))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(foldername))
        print("New version deployed!")
        return True
    except:
       return False

 
