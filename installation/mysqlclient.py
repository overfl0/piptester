from installation._common import apt_install


def linux():
    apt_install('libmysqlclient-dev')
