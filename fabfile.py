import sys
from fabric.api import *


env.skip_bad_hosts = True
def read_hosts():
    env.hosts = open('host_files', 'r').readlines()


def userdel():
    if run("grep rhwang /etc/passwd", warn_only=True).succeeded:
                run("sudo /usr/sbin/userdel rhwang")
                print("removing user")
    else:
                print("User does not exist")
