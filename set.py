# ------------#
# //* Sets --> collection which is unordered , un-indexing , no duplicate values.

fruits = {"apple", "orange", "banana", "pineapple", "watermelon", "banana"}
more_fruits = {"Blackberry", "Cherry", "Grape", "Lemon", "banana"}

for fruits in fruits:
    print(fruits, "", end="")  # they aren't in a order from

# //* Sets methods
# Add -->Adds an element to the set
fruits.add("Jackfruit")
print(fruits)

# Clear --> Removes all the elements from the set
fruits.clear()
print(fruits)

# Copy --> Returns a copy of the set
copy = fruits.copy()
print(copy)

# Difference --> Returns a set containing the difference between two or more sets
difference = fruits.difference(more_fruits)
difference = fruits - more_fruits  # This method can also be written in short (-)
print(difference)
print(difference)

# Discard --> Removes the items in this set that are also included in another, specified set
fruits.discard("pineapple")
print(fruits)

# Intersection --> 	Returns a set, that is the intersection of two other sets
intersection = fruits.intersection(more_fruits)
intersection = fruits & more_fruits  # This method can also be written in short (&)
print(intersection)

# Pop --> Removes an element from the set
fruits.pop()
print(fruits)

# Remove --> Removes the specified element
fruits.remove("banana")
print(fruits)
