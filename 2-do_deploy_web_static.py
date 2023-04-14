#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from fabric.api import env
from fabric.api import run
import os


env.hosts = ['35.153.93.29', '54.146.57.141']
env.user = 'ubuntu'
env.key_filename = '~/ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0] 
    status = True
    try:
        with cd('/tmp/'):
            put(archive_path)
        sudo('mkdir -p /data/web_static/release/{}'.format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_path, name))
        run('rm -rf /tmp/{}'.format(archive_path))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases/{} /data/web_static/current'.format(name))
        return status
    except Exception as e:
        status = False
        return status 
