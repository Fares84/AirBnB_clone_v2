#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static
that distributes an archive to web server, using
the function do_deploy """
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local
from datetime import datetime
from os import path

env.hosts = ['34.73.62.68', '34.75.147.36']
env.user = "ubuntu"


def do_pack():
    """ generate a compressed archive
    the function do_pack must return the archive path
    if the archive has been correctly generated
    otherwise, it should return None
    """
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
    """distributes an archive to web server
    Args:
        archive_path (path): path of the archive file
    """
    if not path.exists(archive_path) and path.isfile(archive_path):
        return False
    file_name = archive_path.split("/")[-1].split(".")[0]
    folderpath = "/data/web_static/releases/{}/web_static/*".format(file_name)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(file_name, file_name))
        run("sudo rm /tmp/{}.tgz".format(file_name))
        run("sudo mv {} /data/web_static/releases/{}/".format
            (folderpath, file_name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(file_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        return True
    except:
        return False
    return True
