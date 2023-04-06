import os
import shutil

# define the path to your desktop
desktop_path = os.path.expanduser("~/Desktop")

# create a dictionary to hold the file extensions and their corresponding directories
ext_dirs = {}

# loop through all files on the desktop
for file_name in os.listdir(desktop_path):
    # get the extension of the file
    ext = os.path.splitext(file_name)[1]

    # if the file has an extension
    if ext:
        # create a directory for the extension if it doesn't exist
        if ext not in ext_dirs:
            ext_dir = os.path.join(desktop_path, ext[1:].upper() + " Files")
            os.makedirs(ext_dir, exist_ok=True)
            ext_dirs[ext] = ext_dir

        # move the file to the corresponding directory
        src_file_path = os.path.join(desktop_path, file_name)
        dest_file_path = os.path.join(ext_dirs[ext], file_name)
        shutil.move(src_file_path, dest_file_path)
        print(f"Moved {file_name} to {ext_dirs[ext]}")