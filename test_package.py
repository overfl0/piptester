import argparse
import importlib
import os
import sys

import pkg_resources

sys.path.append(os.path.dirname(__file__))


from workarounds import CUSTOM_PACKAGE_REQUIREMENTS, PACKAGE_IMPORT_NAME
from common import mark_as_installed_successfully, verbose_run, CURRENT_OS


def try_installing(package):
    # if has_installed_successfully(package):
    #     print(f'Package {package} was previously installed successfully, skipping...', flush=True)
    #     return

    try:
        installation = importlib.import_module(f'installation.{package}')
        installation_helper = getattr(installation, CURRENT_OS)
    except ModuleNotFoundError:
        pass
    except AttributeError:
        pass
    else:
        installation_helper()

    pip_args = ['--no-warn-script-location', '--disable-pip-version-check', '--cache-dir', 'cache']

    if package in CUSTOM_PACKAGE_REQUIREMENTS:
        print(f'Installing implicit {package} requirements...')
        cmd = [sys.executable, '-I', '-E', '-s', '-m', 'pip', 'install'] + pip_args + CUSTOM_PACKAGE_REQUIREMENTS[package]
        verbose_run(cmd)

    print(f'Installing {package}...')
    cmd = [sys.executable, '-I', '-E', '-s', '-m', 'pip', 'install'] + pip_args + [package]
    verbose_run(cmd)

    cmd = [sys.executable, '-I', '-E', '-s', 'test_package.py', 'test', package]
    verbose_run(cmd)


def guess_import_name(package):
    try:
        return PACKAGE_IMPORT_NAME[package]
    except KeyError:
        import_name = package

    dist_path = pkg_resources.get_distribution(import_name).egg_info

    try:
        # print('###')
        # print(open(os.path.join(dist_path, "top_level.txt")).read())
        # print('$$$')
        lines = []
        for line in open(os.path.join(dist_path, "top_level.txt")).read().strip().splitlines():
            lines.append(line.replace('/__init__', '').replace('/', '.'))

        # If we have a matching import
        if import_name in lines:
            return import_name

        if import_name.startswith('python-') and import_name[7:] in lines:
            return import_name[7:]

        return lines[-1]

    except FileNotFoundError:
        print('Could not find the top_level.txt file, guessing module name:', import_name)

    # Heuristics
    module_name = import_name.replace('-', '_')
    if module_name.endswith('_cffi'):
        module_name = module_name[:-5]

    return module_name


def test_package(package):
    import_name = guess_import_name(package)
    print(f'Importing {import_name}...', flush=True)

    running_helper = None
    try:
        running = importlib.import_module(f'running.{package}')
        running_helper = getattr(running, CURRENT_OS)
    except ModuleNotFoundError:
        pass
    except AttributeError:
        pass

    if running_helper:
        running_helper()
    else:
        importlib.import_module(import_name)

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
