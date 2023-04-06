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
        
def delete_directory(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"{dir_path} deleted successfully!")
    except Exception as e:
        print(f"Error deleting {dir_path}: {e}")
        
        
        
# Example usage

create_file("test.txt")

# rename a file
rename_file("test.txt", "new_test.txt")

# copy a file
copy_file("new_test.txt", "test_copy.txt")

# delete a file
delete_file("new_test.txt")

# create a directory
create_directory("test_dir")

# rename a directory
rename_directory("test_dir", "new_test_dir")

# delete a directory
delete_directory("new_test_dir")
