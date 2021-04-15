#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static
that distributes an archive to web server, using
the function do_deploy"""
from fabric.api import local
from fabric.api import env
from fabric.api import run
from fabric.api import put
from datetime import datetime
from os import path

env.hosts = ['34.73.62.68', '34.75.147.36']
env.user = "ubuntu"

def do_deploy(archive_path):
    """ distributes an archive to web server
    Args:
        archive_path (path): path of the archive file 
    """
    if not path.exists(archive_path):
        return False
    try:
        # var to get the file name only separated by / and get last pos
        filename = archive_path.split("/")[-1]
        # set var for path to unompr and set only the compressed file
        # without the exetension, divided by "." and first[0] position
        folderpath = ("/data/web_static/releases/" + 
                      filename.split(".")[0])
        # upload the archive_path tp tmp on the server
        put(archive_path, "/tmp/")
        # run is used to execute a shell command on remote servers
        run("mkdir -p {}".format(folderpath))
        # uncompress archive to specific folder using -C
        # tar compresses multiple files
        run("tar -xzf /tmp/{} -C {}".format(filename,
                                            folderpath)) 
        # delete the archive from the web server
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(folderpath,
                                            folderpath))
        run("rm -rf {}/web_static".format(folderpath))
        # delete symbolic link
        run("rm -rf /data/web_static/current")
        #create a new symbolic link ln -s /usr/local/var /var/run
        run("sudo ln -s {} /data/web_static/current".format(folderpath))
        return True
    except:
        return False
