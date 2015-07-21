import sys
from fabric.api import *
from functools import partial

env.colorize_errors = True
env.skip_bad_hosts = True
def read_hosts():
    env.hosts = open('host_files', 'r').readlines()


def hosts():
    with open("host_files", "r") as f:
        env.hosts = [line.strip() for line in f if not line.startswith('#')]

def memory():
     run('free -m')


def userdel():
    if run("grep rhwang /etc/passwd", warn_only=True).succeeded:
                run("sudo /usr/sbin/userdel rhwang")
                print("removing user")
    else:
                print("User does not exist")
