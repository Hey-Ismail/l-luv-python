# ------------------#
# //* String methods
# //*Capitalize --> Converts the first character to upper case
my_name = "ISMAIL HOSSAIN FAHIM"
print(my_name.capitalize())

# //* center -->Returns a centered string
my_name = "Ismail"
print(my_name.center(10))

# //* count -->Returns the number of times a specified value occurs in a string
my_name = "Ismail Hossain Fahim"
print(my_name.count("a"))

# //* find --> Searches the string for a specified value and returns the position of where it was found
my_name = "Ismail Hossain Fahim"
print(my_name.find(" "))

# //* formate -->Formats specified values in a string
txt = "My name is :{name}"
print(txt.format(name="Ismail Hossain Fahim"))

# //* index --> Searches the string for a specified value and returns the position of where it was found
my_name = "ismail Hossain fahim"
print(my_name.index("H"))

# //* replace --> Returns a string where a specified value is replaced with a specified value
txt = "I love burger "
print(txt.replace("burger", "pizza"))

# //* Split --> Splits the string at the specified separator, and returns a list
txt = "This is a text"
print(txt.split())

# //* startswith --> Returns true if the string starts with the specified value
txt = "This text starts with ''T''"
print(txt.startswith("T"))

# //* Strip -->Returns a trimmed(Remove spaces at the beginning and at the end of the string) version of the string
txt = "             trimmedtxt                 "
print(txt.strip())

# //* swapcase --> Swaps cases, lower case becomes upper case and vice versa
txt_upper = "this will show in uppercase"
txt_lower = "THIS WILL SHOW IN LOWERCASE"
print(txt_upper.swapcase())
print(txt_lower.swapcase())
