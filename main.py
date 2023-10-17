import os
import subprocess

# Dictionary that maps the relevant bash command for each file format
# to the correct file extension for that format
file_formats = dict(flac='.flac', aif='.aiff', alac='.m4a', wav='.wav', mp3='.mp3')

folder = input("Provide full path to folder: ")

# Ensure the folder path is valid
if not os.path.exists(folder):
    print("Invalid folder path provided. Exiting.")
    exit()

output_format = input("Specify the format of the output file(s). Choose from one of flac, aif, alac or wav: ")

# Validate output format
if output_format not in file_formats:
    print("Invalid output format provided. Exiting.")
    exit()

output_dir = input("Enter the desired output directory: ")

for root, dirs, files in os.walk(folder):
    # First replicate the directory structure of the folder inside the output directory
    for name in dirs:
        dir_path = os.path.join(root, name)
        relative_path = os.path.relpath(dir_path, folder)
        new_dir = os.path.join(output_dir, relative_path)
        os.makedirs(new_dir, exist_ok=True)

    for name in files:
        if name.startswith('.'):  # Skip hidden files
            continue

        file_path = os.path.join(root, name)
        extension = os.path.splitext(file_path)[1].lower()

        if extension == file_formats[output_format]:
            print(f"Output format same as input for {name}, skipping file.")
            continue

        if extension not in file_formats.values():
            print(f"Invalid input file {name}, skipping file.")
            continue

        relative_path = os.path.relpath(file_path, folder)
        outpath = os.path.join(output_dir, os.path.dirname(relative_path))

        # Construct the bash command using list arguments
        bash_command = ["/Applications/XLD.app/Contents/MacOS/xld", "-f", output_format, file_path, "-o", outpath]

        # Process each file and handle potential errors from the subprocess
        try:
            subprocess.run(bash_command, check=True)
            print(f"Processed file: {name}")
        except subprocess.CalledProcessError:
            print(f"Error processing file: {name}")

print("Finished processing all files.")