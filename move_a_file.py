# ---------------------#
# //* move-a-file --> it will move a file
import os

# src --> the file that yoy want to move
# destination --> where you want to move the file

src = input("Enter the src path\n-->")
destination = input("Enter where you want to move the 'src' content\n-->")

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(src, destination)  # two parameters
        print(src, " was moved successfully")

except FileNotFoundError:
    print(src, "path does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
