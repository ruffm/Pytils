import os
import sys

filename = sys.argv[1]
userID = sys.argv[2]
groupID = sys.argv[3]

os.chown(filename, userID, groupID)

