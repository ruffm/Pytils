import sys
import os

filename = sys.argv[1]

fileToManipulate = open(filename, 'r')
for line in fileToManipulate:
    line = line.split()
    line.sort()
    print(' '.join(line))
fileToManipulate.close()
