#!/usr/bin/python3
from fabric.api import put 
from fabric.api import env
from fabric.api import run
import os

env.user = 'ubuntu'
env.hosts = ['54.144.46.42', '100.25.194.141']


def do_deploy(archive_path):
    """
    Distributes an archive file to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        put(archive_path, "/tmp/{}".format(archive_filename))
        archive_folder = archive_filename.replace('.tgz', '')
        run("sudo mkdir -p /data/web_static/releases/{}"
            .format(archive_folder))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(archive_filename, archive_folder))
        run("sudo rm -rf /tmp/{}".format(archive_file))
        run("sudo mv /data/web_static/releases/{}/web_static/* "\
            "/data/web_static/releases/{}"
            .format(archive_folder, archive_folder))
        run("sudo rm -rf /data/web_static/releases/{}/web_static/"
            .format(archive_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} "\
            "/data/web_static/current".format(archive_folder))
        print("New version deployed!")
        return True
    except:
        return False
        

