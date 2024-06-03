# -------------#
# //* Write-a-file --> It will help us to write / edit a file
path = input("Enter the file path\n-->")
text = input("What you want to write\n-->")

#'+a' means to append and read file
#'w' means to write a file
try:
    with open(path, "a+") as file:
        content = file.read()
        file.write(text)  # Will write what we want to write

except FileNotFoundError:
    print("This file dose't exits")

else:
    print(content)
