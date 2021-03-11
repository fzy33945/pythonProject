#--coding:utf-8--
# 在C:\Users\<用户名>\pip目录下，创建pip.ini，更换pip第三方安装源地址至国内清华镜像源
import os

# pip.ini的内容
content = '''[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn'''

def main():
    # 目标目录
    dir_path = "c:\\users\\" + os.getlogin() + "\\pip"
    # 创建目标目录
    try:
        os.mkdir(dir_path)
    except:
        print("----目标目录已经存在，跳过执行----")
    # 目标路径
    file_path = dir_path + "\\pip.ini"
    # 写入
    pip_ini_hdl = open(file_path, "w")
    global content
    pip_ini_hdl.write(content)
    pip_ini_hdl.close()
    print("----安装源已经成功更换！----")
    stop = input()

main()