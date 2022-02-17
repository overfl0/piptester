import argparse
import importlib
import os
import subprocess
import sys

import pkg_resources


MARK_INSTALLED_DIR = os.path.join('cache', 'installed')
MARK_FAILED_DIR = os.path.join('cache', 'failed')


def has_previously_installed_successfully(package):
    package_file = os.path.join(MARK_INSTALLED_DIR, package)
    return os.path.exists(package_file)


def mark_as_installed_successfully(package):
    print(f'MARKING {package} AS SUCCESSFUL!')
    os.makedirs(MARK_INSTALLED_DIR, exist_ok=True)
    package_file = os.path.join(MARK_INSTALLED_DIR, package)
    with open(package_file, 'wb'):
        pass


def mark_as_failed(package):
    os.makedirs(MARK_FAILED_DIR, exist_ok=True)
    package_file = os.path.join(MARK_FAILED_DIR, package)
    with open(package_file, 'wb'):
        pass


def verbose_run(cmd):
    print(' '.join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def try_installing(package):
    if has_previously_installed_successfully(package):
        print(f'Package {package} was previously installed successfully, skipping...', flush=True)
        return

    print(f'Installing {package}...')
    pip_args = ['--no-warn-script-location', '--disable-pip-version-check', '--cache-dir', 'cache']
    cmd = [sys.executable, '-I', '-E', '-s', '-m', 'pip', 'install'] + pip_args + [package]
    verbose_run(cmd)

    cmd = [sys.executable, '-I', '-E', '-s', 'test_package.py', 'test', package]
    verbose_run(cmd)


def test_package(package):
    dist_path = pkg_resources.get_distribution(package).egg_info
    try:
        module_name = open(os.path.join(dist_path, "top_level.txt")).read().strip().splitlines()[-1].replace('/', '.')
    except FileNotFoundError:
        module_name = package.replace('-', '_')
        print('Could not find the top_level.txt file, guessing module name:', module_name)
    print(f'Importing {package}...', flush=True)
    importlib.import_module(module_name)
    mark_as_installed_successfully(package)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['install', 'test'])
    parser.add_argument('package')
    args = parser.parse_args()

    if args.command == 'install':
        try_installing(args.package)
    elif args.command == 'test':
        test_package(args.package)
    else:
        raise ValueError('Incorrect command')
