#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from fabric.api import env
from fabric.api import run
import os


env.hosts = ['18.233.66.135', '18.207.141.188']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False
    status = True

    try:
        tgz_file = os.path.basename(archive_path)
        put(archive_path, "/tmp/{}".format(tgz_file))
        dir_name = tgz_file.replace('.tgz', '')      
        run("sudo mkdir -p /data/web_static/releases/{}".format(dir_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(tgz_file, dir_name))
        run("sudo rm -rf /tmp/{}".format(tgz_file))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".format(dir_name))
        print("New version deployed!")
        return status
    except Exception as err:
        status = False
        return status
        
