import os


path = "\Desktop\HelloWorld.txt"

try:
    os.rmdir(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)
