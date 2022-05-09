import argparse
import json
import os
import sys
import urllib.request

from tqdm import tqdm

from blacklist import BLACKLIST
from common import has_installed_successfully, mark_as_failed, chunks, mark_as_installed_successfully, \
    verbose_run_and_tee, LOGS_DIR
from workarounds import PACKAGES_REAL_NAME

URL = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json'
FILENAME = 'top-pypi-packages-30-days.json'
ABS_FILE = os.path.join(os.path.dirname(__file__), FILENAME)
COUNT = 1000


def try_installing(package, linux=False):
    if linux:
        interpreter = '/python/python-39-embed-linux64/bin/python3'
        docker = ['docker', 'run', '--rm', '-w', '/data',
                  '-v', f'{os.path.abspath(os.path.dirname(__file__))}:/data',
                  'piptester']
    else:
        interpreter = 'c:/python-39-embed-amd64/python.exe'
        docker = ['docker', 'run', '--rm', '-w', 'c:\\data',
                  '-v', f'{os.path.abspath(os.path.dirname(__file__))}:c:\\data',
                  'piptester']

    cmd = docker + [interpreter, 'test_package.py', 'install', package]

    try:
        rc, output = verbose_run_and_tee(cmd, timeout=120)
        if rc:
            mark_as_failed(package, output)
    except KeyboardInterrupt:
        sys.exit(1)

    # Re-mark as successful but this time along with the installation logs
    if has_installed_successfully(package):
        mark_as_installed_successfully(package, output)

    # print(output.decode('utf8', 'replace'))
    with open(os.path.join(LOGS_DIR, package + '.txt'), 'wb') as f:
        f.write(output)


def main(args):
    if args.package:
        try_installing(PACKAGES_REAL_NAME.get(args.package, args.package), linux=args.linux)
        return

    data = list(chunks(get_pypi_package_names()['rows'], 50))[args.chunk]

    for row in tqdm(data[:COUNT]):
        project = row['project']
        project = PACKAGES_REAL_NAME.get(project, project)
        if project in BLACKLIST:
            continue

        if has_installed_successfully(project):
            print(f'Skipping {project}')
            continue

        print('\r' + '#' * 80)
        print(project)

        try_installing(project, linux=args.linux)


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
    parser = argparse.ArgumentParser()
    parser.add_argument('--linux', action='store_true', default=sys.platform == 'linux')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--chunk', type=int)
    group.add_argument('--package', type=str)
    args = parser.parse_args()

    main(args)


# docker build -t piptester .
