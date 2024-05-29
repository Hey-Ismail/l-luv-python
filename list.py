# -----------#
# //* Lists --> Its used to store multiple items ina single variable.

cars = ["mercedes-benz", "BMW", "porsche", "mclaren", "Audi"]
for_extend = ["lamborghini", "Toyota-Supra", "maybach", "Rolls-Royce", "Ford"]
print("My favorite car brands :" + str(cars))

for i in cars:
    print(i, "", end="")
# //* List methods

# Append -->  # Adds an element at the end of the list
cars.append("Ferrari")
print(cars)

# Clear --> # Removes all the elements from the list
cars.clear()
print(cars)

# Copy -> # Returns a copy of the list
demo = cars.copy()
print(demo)
print(cars)

# Count --> # Returns the number of elements with the specified value
print(cars.count("mclaren"))

# Extend -->  # Add the elements of a list (or any iterable), to the end of the current list
cars.extend(for_extend)
print(cars)

# Index --> # Returns the index of the first element with the specified value
index = cars.index("porsche")
print(index)

# Insert -->  # Adds an element at the specified position
cars.insert(3, "Toyota-Supra")
print(cars)

# Pop -->  # Removes the first item with the specified value
cars.pop(4)
print(cars)

# Remove --> # Removes the first item with the specified value
cars.remove("Audi")
print(cars)

# Reverse --> # Reverses the order of the list
cars.reverse()
print(cars)

# Sort -->  # Sorts the list
cars.sort()
print(cars)
