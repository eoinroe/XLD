# !/usr/bin/python

import os
import subprocess

# Explore this as a way of checking what causes the cannot process file error:
# https://stackoverflow.com/questions/18460186/writing-outputs-to-log-file-and-console

# Need to create a dictionary to map file format names  
# to file extension names and the relevant bash command  
file_formats = {
    'flac' : '.flac',
    'aiff' : '.aiff',
    'alac' : '.m4a',
    'wav'  : '.wav'
}


# Python 3.6 uses the input() method
# Provide full path to folder
sample_pack = raw_input("Enter folder name: ")

# Add exception handling that checks the file format 
# entered is contained within the dictionary
output_format = raw_input("Enter ouput format: ")

for root, dirs, files in os.walk(sample_pack):
    for name in files:
        file_path = os.path.join(root, name)
        #print(file_path)

        # Get the directory that the current file resides in
        dir_path = os.path.dirname(file_path)

        # Get the file extension
        extension = os.path.splitext(file_path)[1]

        # Skips to the next file if the output format is the same as the input
        if extension == file_formats[output_format]: 
            print("Output format same as input, skipping file.")            
            continue 

        # Use subprocess.run() on Python 3.5+
        bash_command = "/Applications/xld -f %s %s -o %s" % (output_format, file_path, dir_path)

        # Use subprocess.check_call() to force an exception if process causes error
        subprocess.call(bash_command, shell=True)

        bash_command = "rm %s" % (file_path)
        subprocess.call(bash_command, shell=True)
