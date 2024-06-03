# ------------------#
# //* copy-a-file --> It allows us to copy a file

# copyfile()--> copies content of a file
# copy() --> copyfile() + permission mode + destination can be directory
# copy2() --> copy() + copies metadata (file's creation and modification times)

import shutil

path = input("Where you want to copy\n-->")
try:
    shutil.copy("text.txt", path)  # src file and another one is destination
except FileNotFoundError:
    print("The location where you want to copy doesn't exist")

else:
    print("Successfully copied !!!")
