# !/usr/bin/python

import os
import subprocess

# Python 3.6 uses the input() method
sample_pack = raw_input("Enter folder name: ")
output_format = raw_input("Enter ouput format: ")

for root, dirs, files in os.walk(sample_pack):
    for name in files:
        file_path = os.path.join(root, name)
        dir_path = os.path.dirname(file_path)

        # Skips to the next file if th output format is the same as the input
        if file_path.endswith(output_format):
            print("Output format same as input, skipping file.")            
            continue 

        # Use subprocess.run() on Python 3.5+
        bash_command = "/Applications/xld -f %s %s -o %s" % (output_format, file_path, dir_path)

        # Use subprocess.check_call() to force an exception if process causes error
        subprocess.call(bash_command, shell=True)

        bash_command = "rm %s" % (file_path)
        subprocess.call(bash_command, shell=True)
