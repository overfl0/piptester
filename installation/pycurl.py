from installation._common import apt_install


def linux():
    apt_install('libcurl4-openssl-dev', 'libssl-dev')
