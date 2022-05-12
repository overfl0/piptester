import os

APT_UPDATED = False


def apt_update(force=False):
    global APT_UPDATED
    if APT_UPDATED and not force:
        return

    cmd = 'apt update'
    print(cmd, flush=True)
    os.system(cmd)

    APT_UPDATED = True


def apt_install(*packages):
    apt_update()
    cmd = 'apt install -y ' + ' '.join(packages)
    print(cmd, flush=True)
    os.system(cmd)


def install_clang():
    apt_install('clang')
