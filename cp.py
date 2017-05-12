import shutil
import sys

origFile = sys.argv[1]
destFile = sys.argv[2]

shutil.copy(origFile, destFile)
