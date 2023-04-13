#!/usr/bin/python3
from fabric.api import Connection
import sys

archive_path = sys.argv[1]
def do_deploy(archive_path):
    env.key_filename = sys.argv[3]
    env.user = sys.argv[5]
    
    con = Connection(user=
