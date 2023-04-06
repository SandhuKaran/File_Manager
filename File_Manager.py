import os
import shutil


def create_file(file_path):
    try:
        with open(file_path, 'w') as f:
            print(f"{file_path} created successfully!")
    except Exception as e:
        print(f"Error creating {file_path}: {e}")


def rename_file(file_path, new_name):
    try:
        os.rename(file_path, new_name)
        print(f"{file_path} renamed to {new_name} successfully!")
    except Exception as e:
        print(f"Error renaming {file_path}: {e}")


def copy_file(file_path, dest_path):
    try:
        shutil.copy2(file_path, dest_path)
        print(f"{file_path} copied to {dest_path} successfully!")
    except Exception as e:
        print(f"Error copying {file_path}: {e}")


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} deleted successfully!")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")


def create_directory(dir_path):
    try:
        os.makedirs(dir_path)
        print(f"{dir_path} created successfully!")
    except Exception as e:
        print(f"Error creating {dir_path}: {e}")


def rename_directory(dir_path, new_name):
    try:
        os.rename(dir_path, new_name)
        print(f"{dir_path} renamed to {new_name} successfully!")
    except Exception as e:
        print(f"Error renaming {dir_path}: {e}")
