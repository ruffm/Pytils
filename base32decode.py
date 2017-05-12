import base64
import sys

textToDecode = sys.argv[1]

textToDecode = base64.b32decode(textToDecode)
print(textToDecode)
