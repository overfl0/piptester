import os

from installation._common import apt_install, windows_refresh_path


def linux():
    apt_install('nodejs')


def windows():
    os.system('choco install -y nodejs')
    windows_refresh_path()
