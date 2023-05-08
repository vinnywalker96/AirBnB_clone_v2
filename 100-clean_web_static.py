#!/usr/bin/python3
from fabric.api import local
from fabric.api import run
from fabric.api import env
from fabric.context_managers import cd
from fabric.context_managers import lcd
import os


env.hosts = ["54.144.46.42", "100.25.194.141"]
env.user = "ubuntu"


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0 or number == 1:
        number = 1
    else:
        number += 1
    with lcd('versions'):
        local('ls -1t | tail -n +{} | xargs rm -rf --'
              .format(number))
    with cd('/data/web_static/releases'):
        run('ls -1t | tail -n +{} | xargs rm -rf --'
            .format(number))
        run('ls -1 | grep -v ^current | xargs -I {} rm -rf -- ./{}')
