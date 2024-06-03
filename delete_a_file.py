# ------------------#
import os
import shutil

path = input("Enter the path to delete a folder\n-->")

try:
    # os.remove(path)  # it will delete a file
    # os.rmdir(path)  # It will delete a empty directory
    shutil.rmtree(path)  # It will delete the directory containing file
except FileNotFoundError:
    print("path,' doesn't exist")
except PermissionError:
    print("You dont have the permission to delete it")
except OSError as e:
    print(e)
else:
    print("successfully deleted ")
