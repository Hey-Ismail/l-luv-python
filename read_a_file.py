# ---------------#
# //* Read file --> it will help us to read file

# this is basic code that shows how to read a file.
# with open("text.txt") as file:
#     print(file.read())
# print(file.closed)

path = input("Enter the path\n->")

try:
    with open(path) as file:
        contain = file.read()
except FileNotFoundError:
    print("This file doesn't exits")

else:
    print(contain)
    # file.close()
