#多账户配置初始化
import sys,os
from multi_account_config import multi_account_config_dic

print(multi_account_config_dic)

#切换工作目录 ~/.ssh/
user_main_home = os.path.expanduser('~')
ssh_dir = os.path.join(user_main_home,".ssh")
print(ssh_dir)
python_file_path = os.getcwd()
os.chdir(ssh_dir)

#1.创建rsa私钥公钥
#ssh-keygen -t rsa -f [rsa_file_name] -C "[email]" -N ''      (-N "" )不用输入密码
ssh_keygen_cmd_template = r'ssh-keygen -t rsa -f %s -C "%s" -N ""'

for host in multi_account_config_dic:
    cmd = ssh_keygen_cmd_template % (multi_account_config_dic[host]['rsa_file_name'],multi_account_config_dic[host]['email'])
    print("ssh-keygen cmd:\t",cmd)
    os.system(cmd)

#2.创建ssh config文件
with open(os.path.join(ssh_dir,"config"),mode="w") as f:
    line_template = "%s %s\n"
    for host in multi_account_config_dic:
        f.write(line_template % ("Host",host))
        f.write(line_template % ("Hostname",host))
        f.write(line_template % ("User",multi_account_config_dic[host]["user"]))
        f.write(line_template % ("IdentityFile","~/.ssh/" + multi_account_config_dic[host]["rsa_file_name"]))
        f.write("\n")


#3.打印ssh_pub
os.chdir(python_file_path)
with open("pub_info.txt",mode="w") as info_f:
    for host in multi_account_config_dic:
        ssh_pub_file_path = os.path.join(ssh_dir,multi_account_config_dic[host]["rsa_file_name"]) + ".pub"
        #print(ssh_pub_file_path)
        with open(ssh_pub_file_path) as f:
            info = host + "\n" + f.read() + ""
            print(info)
            info_f.write(info + "\n")

