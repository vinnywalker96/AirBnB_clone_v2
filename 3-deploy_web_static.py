#!/usr/bin/python3

from datetime import datetime
from fabric.api import env
from fabric.api import run
from fabric.api import put
from fabric.api import local
import os

env.hosts = ['18.233.66.135', '18.207.141.188']
env.user = 'ubuntu'


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(current_time)
        folder_name = "versions"
        local("mkdir -p {}".format(folder_name))
        local("tar -cvzf {}/{} web_static".format(folder_name, file_name))
        return "{}/{}".format(folder_name, file_name)
    except:
        return None


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

    try:
        tgz_file = os.path.basename(archive_path)
        put(archive_path, "/tmp/{}".format(tgz_file))
        dir_name = tgz_file.replace('.tgz', '')
        run("mkdir -p /data/web_static/releases/{}".format(dir_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgz_file, dir_name))
        run("rm -rf /tmp/{}".format(tgz_file))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(dir_name, dir_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(dir_name))
        print("New version deployed!")
        return True
    except Exception as err:
        return False


def deploy():
    """Creates and distribute an archive to a web server."""
    archive_path = do_pack()
    if not archive_path:
        return False
    print(archive_path)
    deploy_status = do_deploy(archive_path)
    return deploy_status
