import subprocess


def linux():
    subprocess.run([r'/python/bin/mkdocs'], check=True)


def windows():
    subprocess.run([r'c:\python\Scripts\mkdocs.exe'], check=True)
