import os
import sys
import platform

dir = sys.argv[1]

if os.name == 'posix':
   if os.path.isdir(dir):
       pwd = os.cwd()
       absolutePath = os.path.abspath(pwd + "/" + dir)
   else:
       print("Not a directory.")

elif platform.system() == 'Windows':
    if os.path.isdir(dir):
        pwd = os.getcwd()
        # dir = pwd + "\\" + dir
        absolutePath = os.path.abspath(pwd + "\\" + dir)
        # print absolutePath # test print of absolutePath
        cd = os.chdir(absolutePath)
    else:
        print("Not a directory.")

else:
    print("What operating system are you on?")