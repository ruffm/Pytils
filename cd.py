import os
import sys

dir = sys.argv[1]

if os.path.isdir(dir):
    pwd = os.getcwd()
    dir = pwd + "\\" + dir
    absolutePath = os.path.abspath(dir)
    # print dir
    cd = os.chdir(dir)

else:
    print("Not a directory.")