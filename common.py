import os
import shutil
import stat
import subprocess
import sys
import time
from contextlib import contextmanager

LOGS_DIR = os.path.join('logs', 'linux' if sys.platform == 'linux' else 'windows')
MARK_INSTALLED_DIR = os.path.join(LOGS_DIR, 'installed')
MARK_FAILED_DIR = os.path.join(LOGS_DIR, 'failed')


@contextmanager
def ignore_no_file():
    try:
        yield
    except FileNotFoundError:
        pass


def print_and_delete(message, *path):
    print(message)
    full_path = os.path.realpath(os.path.join(*path))
    if not os.path.exists(full_path):
        return

    if os.path.isfile(full_path):
        os.remove(full_path)
    elif os.path.isdir(full_path):
        shutil.rmtree(full_path)
    else:
        print('Error: I don\'t know what this file type is!')


def has_installed_successfully(package):
    package_file = os.path.join(MARK_INSTALLED_DIR, package + '.txt')
    return os.path.exists(package_file)


def mark_as_installed_successfully(package, output=b''):
    print(f'MARKING {package} AS SUCCESSFUL!')
    os.makedirs(MARK_INSTALLED_DIR, exist_ok=True)
    if os.path.exists(MARK_INSTALLED_DIR):
        print('Directory created successfully', flush=True)
        os.system(f'ls -lad {MARK_INSTALLED_DIR}')
        os.system('id')
    package_file = os.path.join(MARK_INSTALLED_DIR, package + '.txt')
    with open(package_file, 'wb') as f:
        f.write(output)

    if sys.platform == 'linux' and not os.stat(package_file).st_mode & stat.S_IWOTH:
        os.chmod(package_file, 0o777)


def mark_as_failed(package, output=b''):
    print(f'MARKING {package} AS FAILED from MAIN!')
    os.makedirs(MARK_FAILED_DIR, exist_ok=True)
    package_file = os.path.join(MARK_FAILED_DIR, package + '.txt')
    with open(package_file, 'wb') as f:
        f.write(output)

    if sys.platform == 'linux' and not os.stat(package_file).st_mode & stat.S_IWOTH:
        os.chmod(package_file, 0o777)


def verbose_run(cmd, **kwargs):
    print(' '.join(cmd), flush=True)
    return subprocess.run(cmd, check=True, **kwargs)


def verbose_run_and_tee(cmd, timeout=None):
    start_time = time.time()
    full_output = None
    print(' '.join(cmd), flush=True)

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = process.stdout.readline()
        if full_output:  # Yeah, yeah, performance...
            full_output += output
        else:
            full_output = output

        if not output and process.poll() is not None:
            break

        if output:
            print(output.decode('utf8', 'replace').strip(), flush=True)

        if timeout and time.time() - start_time > timeout:
            process.kill()
            print('<killed>')
            full_output += '<killed>' if type(full_output) is str else b'<killed>'

    rc = process.poll()
    return rc, full_output


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    lst = list(lst)
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
