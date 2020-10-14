# !/usr/bin/python

import os
for root, dirs, files in os.walk('DTIFFANY_sample_pack'):
   for name in files:
      path = os.path.join(root, name)

      dir_path = os.path.dirname(path)

      bashCommand = "/Applications/xld -f flac %s -o %s" % (path, dir_path)
      os.system(bashCommand)
      
      bashCommand = "rm %s" % (path)
      os.system(bashCommand)
