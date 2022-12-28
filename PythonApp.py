
import os


path = "\Desktop\HelloWorld.txt"


access_rights = 0o755

try:
    os.mkdir(path, access_rights)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

   