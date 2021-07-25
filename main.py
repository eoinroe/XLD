import os
import subprocess

# Dictionary that maps the relevant bash command for each file format
# to the correct file extension for that format
file_formats = dict(flac='.flac', aif='.aiff', alac='.m4a', wav='.wav')

# Python 3.6 uses the input() method
folder = raw_input("Provide full path to folder: ")

output_format = raw_input("Specify the format of the output file(s). Choose from one of flac, aif, alac or wav: ")

# Specify the path or name of the output file.  If outpath
# is a directory, output file is saved in that directory.
output_dir = raw_input("Enter the desired output directory: ")

# Use os.scandir() in Python 3 - https://docs.python.org/3/library/os.html#os.scandir

# os.walk() can handle spaces in the path but bash cannot
for root, dirs, files in os.walk(folder):
    # First replicate the directory structure of the folder inside of the output directory
    for name in dirs:
        # Compute the relative file path to the directory from the given start directory
        dir_path = os.path.join(root, name)
        relative_path = os.path.relpath(dir_path, folder)

        new_dir = os.path.join(output_dir, relative_path)
        bash_command = 'mkdir "{}"'.format(new_dir)

        # Use subprocess.run() in Python 3.5+
        subprocess.call(bash_command, shell=True)

    for name in files:
        # Make sure not to include any hidden files (.DS_Store)
        if name.startswith('.'):
            continue

        file_path = os.path.join(root, name)

        # Get the file extension
        extension = os.path.splitext(file_path)[1]

        # Skips to the next file if the output format is the same as the input
        if extension == file_formats[output_format]:
            print("Output format same as input, skipping file.")
            continue

        # Compute the relative file path to the given path from the given start directory.
        relative_path = os.path.relpath(file_path, folder)

        # Join the output directory specified by the user to the path of the file relative to the main folder
        outpath = os.path.join(output_dir, os.path.dirname(relative_path))

        # This method makes sure that the file path is quoted
        # to handle cases where there are spaces in the path
        bash_command = '/Applications/xld -f {} "{}" -o "{}"'.format(output_format, file_path, outpath)

        # Use subprocess.check_call() to force an exception if process causes an error
        subprocess.call(bash_command, shell=True)
