# ----------------#
# //* Dictionary -->  A changeable , unordered collection of qunie key:value pairs
# //*                 fast because try use hashing , allow us to access a value quickly.
student_info = {
    "name": "Ismail Hossain Fahim",
    "age": 21,
    "profession": "Student",
    "university": "AIUB",
    "Is_married": "False",
    "Nationality": "Bangladesh",
    "About this user": "Introvert",
}
# Printing the values
print(student_info.items())

# Printing the values with loop
for key, values in student_info.items():
    print(key, ":", values)

# Using get() method
print(student_info["About this user "])
print(student_info.get("sex"))  # It wil return 'none' instead of showing error
print(student_info.get("age"))

# //* Dictionary Methods
# Update --> Updates the dictionary with the specified key-value pairs
student_info.update({"About this user": "Extrovert"})
print(student_info)

# Clear --> Removes all the elements from the dictionary
student_info.clear()
print(student_info)

# Copy --> 	Returns a copy of the dictionary
copy = student_info.copy()
print(copy)

# Fromkeys --> Returns a dictionary with the specified keys and value
this_key = student_info.fromkeys("name")
print(this_key)

# Pop --> 	Removes the element with the specified key
student_info.pop("age")
print(student_info)

# Popitem --> Removes the last inserted key-value pair
student_info.popitem()
print(student_info)

# values --> return the values of the dictionary
student_info.values()
print(student_info)

# Keys --> returns the keys of the dictionary
student_info.keys()
print(student_info)

# Items --> Returns the item of the dictionary
student_info.items()
print(student_info)
