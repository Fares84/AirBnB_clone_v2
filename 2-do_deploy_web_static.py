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

def do_pack():
    """ generate a compressed archive
    the function do_pack must return the archive path
    if the archive has been correctly generated
    otherwise, it should return None"""
    time_stamp = '%Y%m%d%H%M%S'
    _time = datetime.utcnow().strftime(time_stamp)
    _path = "versions/web_static_{}.tgz".format(_time)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(_path))
    if path.exists(_path):
        return _path
    else:
        return None

def do_deploy(archive_path):
    """ distributes an archive to web server
    Args:
        archive_path (path): path of the archive file 
    """
    if not path.exists(archive_path):
          return False
    # var to get the file name only separated by / and get last pos
    file_name = archive_path.split("/")[-1].split(".")[0]
    # set var for path to unompr and set only the compressed file
    # without the exetension, divided by "." and first[0] position
    folder_to_compress = "/data/web_static/releases/{}/web_static/*".format(file_name)
    try:
        # uploading the archive_path to tmp on the server
        put(archive_path, "/tmp/")
        # run is used to execute a shell command on remote servers
        run("sudo mkdir -p /data/web_static/releases/{}/".format(file_name))
        # uncompress archive to specific folder using -C
        # tar compresses multiple files
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(file_name, file_name))
        # delete the archive from the web server
        run("sudo rm /tmp/{}.tgz".format(file_name))
        run("sudo mv {} /data/web_static/releases/{}/".format(folder_to_compress, file_name))
        # delete symbolic link
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(file_name))
        # create a new symbolic link ln -s /usr/local/var /var/run
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        # on the server, create a linked with the current
        return True
    except:
        return False
    return True
