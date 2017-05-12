import base64
import sys

textToEncode = sys.argv[1]

textToEncode = base64.b16encode(textToEncode)
print(textToEncode)