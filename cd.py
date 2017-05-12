import os
import sys

dir = sys.argv[1]

if os.path.isdir(dir):
    pwd = os.getcwd()
    # dir = pwd + "\\" + dir
    absolutePath = os.path.abspath(pwd + "\\" + dir)
    # print absolutePath
    cd = os.chdir(absolutePath)

else:
    print("Not a directory.")