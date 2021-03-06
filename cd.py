import os
import sys
import platform

directory = sys.argv[1]

if os.name == 'posix':
    if os.path.isdir(directory):
        pwd = os.cwd()
        absolutePath = os.path.abspath(pwd + "/" + directory)
        os.chdir(absolutePath)
        os.system("/bin/bash")
    else:
        print("Not a directory.")

elif platform.system() == 'Windows':
    if os.path.isdir(directory):
        pwd = os.getcwd()
        # directory = pwd + "\\" + directory
        absolutePath = os.path.abspath(pwd + "\\" + directory)
        # print absolutePath # test print of absolutePath
        os.chdir(absolutePath)
        os.system("cmd.exe")
    else:
        print("Not a directory.")

else:
    print("What operating system are you on?")
