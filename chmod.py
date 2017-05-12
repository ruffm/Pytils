import os
import sys

filename = sys.argv[1]
mode = sys.argv[2]

os.fchown(filename, mode)