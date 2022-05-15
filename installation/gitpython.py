import os

from installation._common import apt_install, windows_refresh_path


def linux():
    apt_install('git')


def windows():
    os.system('choco install -y git')
    windows_refresh_path()
