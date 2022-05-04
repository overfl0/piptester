import argparse
import json
import os
import subprocess
import sys
import urllib.request

from tqdm import tqdm

from common import has_installed_successfully, mark_as_failed, chunks, mark_as_installed_successfully, \
    verbose_run_and_tee

URL = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json'
FILENAME = 'top-pypi-packages-30-days.json'
ABS_FILE = os.path.join(os.path.dirname(__file__), FILENAME)
PACKAGES_MAPPING = {
    'backports-csv': 'backports.csv',
    'backports-functools-lru-cache': 'backports.functools-lru-cache',
    'backports-tempfile': 'backports.tempfile',
    'backports-weakref': 'backports.weakref',
    'backports-zoneinfo': 'backports.zoneinfo',
    'jaraco-classes': 'jaraco.classes',
    'jaraco-collections': 'jaraco.collections',
    'jaraco-context': 'jaraco.context',
    'jaraco-functools': 'jaraco.functools',
    'jaraco-text': 'jaraco.text',
    'pdfminer-six': 'pdfminer.six',
    'randomstuff-py': 'randomstuff.py',
    'ruamel-yaml': 'ruamel.yaml',
    'ruamel-yaml-clib': 'ruamel.yaml.clib',
}
BLACKLIST = {
    'azure',  # Marked as deprecated
    'azure-keyvault',  # Metapackage, just installs other packages in the top1000
    'azure-mgmt',  # Deprecated
    'azure-mgmt-datalake-nspkg',  # Empty namespace package
    'azure-mgmt-nspkg',  # Empty namespace package
    'azure-nspkg',  # Empty namespace package
    'azureml-dataprep-rslex',  # Not intended for direct installation
    'bs4',  # Dummy package, use beautifulsoup4
    'google-cloud',  # Deprecated empty package

    # Not supported on Windows
    'ansible',  # Doesn't support windows
    'ansible-core',  # Doesn't support windows
    'blessings',  # Requires curses
    'dockerpty',  # Requires fnctl
    'ptyprocess',  # Requires fnctl
    'pystan',  # https://pystan2.readthedocs.io/en/latest/windows.html
    'python-daemon',  # Requires pwd module (also daemons are only on unix)
    'sekkaybot',  # Requires uvloop
    'sh',  # Requires fnctl
    'uvloop',  # Not supported on Windows
    'uwsgi',  # Not supported on Windows

    # Requires DLL or external setup
    'fiona',
    'geopandas',
    'gitpython',
    'graphframes',  # SPARK_HOME
    'opencv-python',
    'pycurl',  # libcurl
    'python-magic',  # libmagic

    # Bug in library
    'flask-oidc',  # https://github.com/puiterwijk/flask-oidc/pull/141
    'jupyterlab-pygments',  # Requires pygments to be installed
    'keras',  # Required tensorflow 2
    'opensearch-py',  # Requires requests to be installed
    'pydeequ',  # Requires pyspark

    # Requires C++ compiler
    'backports.zoneinfo',
    'ciso8601',
    'dbt-snowflake',
    'netifaces',
    'pycrypto',
    'pygobject',
    'pyminizip',
    'python-levenshtein',
    'python-keystoneclient',  # Requires netifaces
    'sasl',
    'snowflake-connector-python',
    'snowflake-sqlalchemy',  # Requires snowflake-connector-python
    'tensorflow-transform',  # Old pyarrow dependency which installs numpy

    # "lolnope" doesn't work
    'constructs',

}
COUNT = 1000


def try_installing(package):
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
    with open(os.path.join('logs', package + '.txt'), 'wb') as f:
        f.write(output)


def main(args):
    if args.package:
        try_installing(PACKAGES_MAPPING.get(args.package, args.package))
        return

    data = list(chunks(get_pypi_package_names()['rows'], 50))[args.chunk]

    for row in tqdm(data[:COUNT]):
        project = row['project']
        project = PACKAGES_MAPPING.get(project, project)
        if project in BLACKLIST:
            continue

        if has_installed_successfully(project):
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
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--chunk', type=int)
    group.add_argument('--package', type=str)
    args = parser.parse_args()

    main(args)


# docker build -t piptester .
