from installation._common import apt_install


def linux():
    apt_install('libgl1', 'libglib2.0-0')
