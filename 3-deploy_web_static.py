#!/usr/bin/python3
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os

env.hosts = ["54.144.46.42", "100.25.194.141"]
env.user = "ubuntu"


def do_pack():
    """
    Generates a .tgz file from the contents of the web_static
    """
    try:
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(current_time)
        folder_name = "versions"
        local("mkdir -p {}".format(folder_name))
        local("tar -cvzf {}/{} web_static".format(folder_name, file_name))
        return "web_static packed: {}/{}".format(folder_name, file_name)
    except:
        return None

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
    except Exception as e:
        return False

def deploy():
    """Create and distribute an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
