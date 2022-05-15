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
    cmd = 'DEBIAN_FRONTEND=noninteractive apt install -q -y ' + ' '.join(packages)
    print(cmd, flush=True)
    os.system(cmd)


def install_clang():
    apt_install('clang')


def windows_refresh_path():
    import winreg

    def get_sys_env(name):
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,
                               r"System\CurrentControlSet\Control\Session Manager\Environment")
        return winreg.QueryValueEx(key, name)[0]

    def get_user_env(name):
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Environment")
        return winreg.QueryValueEx(key, name)[0]

    new_path = os.path.expandvars(get_sys_env('path') + ';' + get_user_env('path'))
    os.environ['PATH'] = new_path
