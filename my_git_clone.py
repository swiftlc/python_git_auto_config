import os,pyperclip
import re
import time

from multi_account_config import multi_account_config_dic

print(os.getcwd())

git_address = pyperclip.paste()
#示例 :git@github.com:swiftlc/SubmoduleInner.git
#print(git_address)
match = re.match(r'^git@(.*?):.*/(\w+)\.git$',git_address)

if match:
    pass
    host = match.group(1)
    project_name = match.group(2)
    #print(host,project_name)

    clone_cmd = "git clone " + git_address
    print(clone_cmd)

    desktop_dir = os.path.join(os.path.expanduser("~"), 'Desktop')
    os.chdir(desktop_dir)
    os.system(clone_cmd)
    host_info = multi_account_config_dic.get(host)
    if host_info:
        project_dir = os.path.join(desktop_dir,project_name)
        os.chdir(project_dir)
        os.system("git config --local user.name " + host_info["user"])
        os.system("git config --local user.email " + host_info["email"])
else:
    print(git_address,"不是有效git地址")


time.sleep(2)