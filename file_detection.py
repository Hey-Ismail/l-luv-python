# --------------#
# //* file detection -->  to the process of checking whether a file exists, determining its type, or identifying its encoding.

import os  # At first we have to import this

try:
    path = input("Enter the path\n-->")

    if os.path.exists(path):
        print("This path exits in your pc!!!")
    if os.path.isfile(path):
        print("This is location refers as a file.")
    if os.path.isdir(path):
        print("This is location refers as a folder.")
    else:
        raise FileExistsError  # this 'raise' will raise the error

except FileExistsError:
    print("This path doesn't exits in your pc!!!")

finally:
    print("This will pop up!!!")
# path_file = "D:\\text.txt"
# path_folder ="D:\\New folder"
