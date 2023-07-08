import os

from installation._common import apt_install, windows_refresh_path


def linux():
    apt_install('curl')
    os.system('curl -fsSL https://deb.nodesource.com/setup_20.x | bash -')
    apt_install('nodejs')


def windows():
    os.system('choco install -y nodejs')
    windows_refresh_path()
