#!/usr/bin/python3
from fabric.api import env
from fabric.api import run

env.hosts = ['54.146.57.141', '35.153.93.29']
env.user = 'ubuntu'

def taskA():
    run('whoami')
