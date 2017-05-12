import sys
import platform

print "Operating System: " + platform.system()
print "OS Version: " + platform.release()
print "OS Minor Version: " + platform.version()
print "Network Name: " + platform.node()
print "Processor Type: " + platform.machine()
print "Processor Details: " + platform.processor()
print "Python Version: " + platform.python_version()

