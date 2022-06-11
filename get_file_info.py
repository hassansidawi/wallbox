import os
from os.path import join
import win32api
import win32security
from win32comext.shell import shell


def request(root_dir):
    file = ''
    with os.scandir(root_dir) as dir_contents:
        for entry in dir_contents:
            file = entry.name.lower()
            if file.endswith('.exe'):
                info = entry.stat()
                print(entry.name)
                print(info.st_size)
                if info.st_size >= 14 * 2 ** 20:
                    return None

                break

    if not file:
        return None
    else:
        filename = join(root_dir, file)
        sd = win32security.GetFileSecurity(filename, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)
        print('File owned by %s\\%s' % (domain, name))

        username = win32api.GetUserNameEx(win32con.NameSamCompatible)
        print('I am', username)
        if shell.IsUserAnAdmin():
            print('user is an admin')
            return filename
        else:
            print('user is not an admin')
            return None
