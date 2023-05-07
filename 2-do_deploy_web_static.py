#!/usr/bin/python3
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os

env.hosts = ["54.144.46.42", "100.25.194.141"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory of web server
        archive_filename = os.path.basename(archive_path)
        put(archive_path, '/tmp/{}'.format(archive_filename))

        # Uncompress archive to /data/web_static/releases/<archive filename without extension> on web server
        archive_folder = archive_filename.replace('.tgz', '')
        run('mkdir -p /data/web_static/releases/{}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_filename, archive_folder))

        # Delete archive from web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete symbolic link /data/web_static/current from web server
        run('rm -rf /data/web_static/current')

        # Create new symbolic link /data/web_static/current on web server
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_folder))

        return True
    except:
        return False

