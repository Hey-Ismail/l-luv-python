# ------------#
# //* Index operators [] --> It gives access to a sequence's elements (str, lists, tuples)

# String
name = "Ismail Hossain Fahim"
if name.capitalize():
    name = name.upper()
    print(name)

first_name = name[:6]
middle_name = name[7:14]
last_name = name[15:]
print(f"{first_name} {middle_name} {last_name}")
print(name[0])
print()
print(name.replace("Ismail Hossain Fahim", "Ismail Hossain"))
print(name.count("a"))
print(name.endswith("m"))

# Lists
name = ["Ismail", "Hossain", "Fahim"]
name.insert(3, "Hossain")
name.append("Ismail")
name.reverse()
name.pop()
name.sort()
name.clear()
name = name.index("Fahim")
print(name)

# Tuples
name = ("Ismail", "Hossain", "Fahim")
name_list = list(name)
name_list.insert(3, "Hossain")
name_list.append("Ismail")
name_list.reverse()
name_list.pop()
name_list.sort()
name = tuple(name_list)
name_list.clear()
name = tuple(name_list)
name = ("Ismail", "Hossain", "Fahim")
index_of_fahim = name.index("Fahim")
print(name)
print("Index of Fahim:", index_of_fahim)
