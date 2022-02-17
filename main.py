import json
import os
import subprocess
import sys
import urllib.request

from tqdm import tqdm

from common import has_previously_installed_successfully, mark_as_failed

URL = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json'
FILENAME = 'top-pypi-packages-30-days.json'
ABS_FILE = os.path.join(os.path.dirname(__file__), FILENAME)
BLACKLIST = {
    'typing-extensions',
}
COUNT = 1000


def try_installing(package):
    interpreter = 'python-37-embed-amd64/python.exe'
    docker = ['docker', 'run', '--rm', '-v', f'{os.path.join(os.getcwd(), "cache")}:c:\\cache', 'piptester']
    cmd = docker + [interpreter, 'test_package.py', 'install', package]
    print(' '.join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        sys.exit(1)
    except:  # noqa
        print(f'MARKING {package} AS FAILED from MAIN!')
        mark_as_failed(package)


def main():
    data = get_pypi_package_names()

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


def get_pypi_package_names():
    if not os.path.isfile(ABS_FILE):
        print('Not in cache, downloading...')
        with urllib.request.urlopen(URL) as f:
            data = f.read().decode('utf-8')
            with open(ABS_FILE, 'w') as fw:
                fw.write(data)

    with open(ABS_FILE) as f:
        data = json.load(f)

    return data


if __name__ == '__main__':
    main()


# docker build -t piptester .
