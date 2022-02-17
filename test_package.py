import argparse
import importlib
import os
import sys

import pkg_resources

from common import has_previously_installed_successfully, mark_as_installed_successfully, verbose_run


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
