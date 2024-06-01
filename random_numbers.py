# ------------#
# //* Random --> it is chosen by system , we have to import random to access random
import random

# Random --> returns a random number
number = random.randint(1, 6)
print(number)

# random --> Returns a random float number between 0 and 1
number = random.random()
print(number)

# Choice -->Returns a random element from the given sequence
myList = ["Rock", "Paper", "Scissors"]
print(random.choice(myList))

# Shuffle -->Takes a sequence and returns the sequence in a random order
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)

# sample --> Returns a given sample of a sequence
fruits = ["apple", "banana", "mango"]
print(random.sample(fruits, k=2))

# uniform --> Returns a random float number between two given parameters
numbers = [10, 20]
random_number1 = numbers[0]
random_number2 = numbers[1]
print(random.uniform(random_number1, random_number2))
