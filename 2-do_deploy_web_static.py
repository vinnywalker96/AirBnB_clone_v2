#!/usr/bin/python3
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os

env.hosts = ["54.144.46.42", "100.25.194.141"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        foldername = filename.split(".")[0]
        path = "/data/web_static/releases/{}".format(foldername)
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}/".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        print("New version deployed!")
        return True
    except:
        return False        
