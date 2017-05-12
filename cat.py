import sys

filename = sys.argv[1]

fileToManipulate = open(filename, 'r')
for line in fileToManipulate:
    print line
fileToManipulate.close()
