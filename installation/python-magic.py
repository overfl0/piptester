import sys

from common import verbose_run
from installation._common import apt_install


def linux():
    apt_install('libmagic1')


def windows():
    pip_args = ['--no-warn-script-location', '--disable-pip-version-check', '--cache-dir', 'cache']
    cmd = [sys.executable, '-I', '-E', '-s', '-m', 'pip', 'install'] + pip_args + ['python-libmagic', 'python-magic-bin']
    verbose_run(cmd)
