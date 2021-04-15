#!/usr/bin/python3
""" Fabric script that generates a compressed file (.tgz) from the contents
    of the web_static folder of your AirBnB Clone repo """
from fabric.api import local
from datetime import datetime
from os import path


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
