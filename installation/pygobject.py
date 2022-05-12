from installation._common import apt_install


def linux():
    apt_install('pkg-config', 'libcairo2-dev', 'libgirepository1.0-dev')
