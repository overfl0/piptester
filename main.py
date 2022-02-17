import os
import subprocess
import json
import os
import subprocess
import sys
import textwrap
import urllib.request

from tqdm import tqdm

URL = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json'
FILENAME = 'top-pypi-packages-30-days.json'
ABS_FILE = os.path.join(os.path.dirname(__file__), FILENAME)
BLACKLIST = {
    'typing-extensions',
}
COUNT = 1000


MARK_INSTALLED_DIR = os.path.join('cache', 'installed')
MARK_FAILED_DIR = os.path.join('cache', 'failed')


def has_previously_installed_successfully(package):
    package_file = os.path.join(MARK_INSTALLED_DIR, package)
    return os.path.exists(package_file)


def mark_as_failed(package):
    os.makedirs(MARK_FAILED_DIR, exist_ok=True)
    package_file = os.path.join(MARK_FAILED_DIR, package)
    with open(package_file, 'wb'):
        pass


def try_installing(package):
    interpreter = 'python-37-embed-amd64/python.exe'
    docker = ['docker', 'run', '--rm', '-v', f'{os.path.join(os.getcwd(), "cache")}:c:\\cache', 'piptester']
    cmd = docker + [interpreter, 'test_package.py', 'install', package]
    print(' '.join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        print(f'MARKING {package} AS FAILED from MAIN!')
        mark_as_failed(package)


def main():
    if not os.path.isfile(ABS_FILE):
        print('Not in cache, downloading...')
        with urllib.request.urlopen(URL) as f:
            data = f.read().decode('utf-8')
            with open(ABS_FILE, 'w') as fw:
                fw.write(data)

    with open(ABS_FILE) as f:
        data = json.load(f)

        for row in tqdm(data['rows'][:COUNT]):
            project = row['project']
            if project in BLACKLIST:
                continue

            if has_previously_installed_successfully(project):
                print(f'Skipping {project}')
                continue
            print('\r' + '#' * 80)
            print(project)
            try_installing(project)


if __name__ == '__main__':
    main()


# docker build -t piptester .