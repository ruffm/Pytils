import sys
import os

origFile = sys.argv[1]
targetFile = sys.argv[2]

os.rename(origFile, targetFile)