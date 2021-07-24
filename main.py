import os
import subprocess

# Explore this as a way of checking what causes the cannot process file error:
# https://stackoverflow.com/questions/18460186/writing-outputs-to-log-file-and-console

# -f: Specify format of decoded file
# 	      wav        : Microsoft WAV (default)
# 	      aif        : Apple AIFF
# 	      raw_big    : Raw PCM (big endian)
# 	      raw_little : Raw PCM (little endian)
# 	      mp3        : LAME MP3
# 	      aac        : MPEG-4 AAC
# 	      flac       : FLAC
# 	      alac       : Apple Lossless
# 	      vorbis     : Ogg Vorbis
# 	      wavpack    : WavPack
# 	      opus       : Opus

# Need to create a dictionary to map file format names
# to file extension names and the relevant bash command
file_formats = dict(flac='.flac', aif='.aiff', alac='.m4a', wav='.wav')

# Python 3.6 uses the input() method
folder = raw_input("Provide full path to folder: ")

# Add exception handling that checks the file format
# entered is contained within the dictionary
output_format = raw_input("Specify the format of the output file(s). Choose from one of flac, aif, alac or wav: ")

# -o outpath 
# Specify the path or name of the output file.  If outpath
# is a directory, output file is saved in that directory.
outpath = raw_input("Enter the desired output directory: ")

# Use os.scandir() in Python 3 - https://docs.python.org/3/library/os.html#os.scandir

# os.walk() can handle spaces in the path but bash cannot
for root, dirs, files in os.walk(folder):
    for name in files:
        file_path = os.path.join(root, name)
        # print(file_path)

        # Get the directory that the current file resides in
        dir_path = os.path.dirname(file_path)

        # Get the file extension
        extension = os.path.splitext(file_path)[1]

        # Skips to the next file if the output format is the same as the input
        if extension == file_formats[output_format]:
            print("Output format same as input, skipping file.")
            continue

        # http://mywiki.wooledge.org/BashPitfalls
        # bash_command = "/Applications/xld -f %s %s -o %s" % (output_format, file_path, dir_path)

        # This method makes sure that the file path is quoted
        # to handle cases where there are spaces in the path
        bash_command = '/Applications/xld -f {} "{}" -o "{}"'.format(output_format, file_path, outpath)

        # Use subprocess.check_call() to force an exception if process causes error
        subprocess.call(bash_command, shell=True)

        # Delete the original file
        # bash_command = "rm %s" % file_path

        # This is dangerous! Specify a directory as outpath instead.
        # bash_command = 'rm "{}"'.format(file_path)

        # Use subprocess.run() in Python 3.5+
        subprocess.call(bash_command, shell=True)
