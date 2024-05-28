# ------------#
# //* Loops ->It's a way to repeat a block of code multiple times.
# //* there are three types of loop in python (while, for and nested-loop)

# While-loop --> A statement that will execute it's block of code(unlimited times), as long as it's condition remains true
guess_the_number = int(input("Guess the number (1-100) :"))
target_number = 69
while not (guess_the_number == target_number):
    print("Incorrect number , try again")
    guess_the_number = int(input("Guess the number (1-100) :"))

print(f"Bingo!!!, your answer {guess_the_number} is correct")

# foo-loop --> A statement that will execute it's block of code(limited times)
for i in range(5):
    print("Ismail Hossain Fahim")

for name in "Ismail Hossain Fahim":
    print(name)

for number in range(0, 10, 2):
    print(number)
# //* printing "happy Birthday" message with a count down using "for-loop".
import time

for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)
print("Happy Birthday!!!")

# nested-loop --> The "Inner loop" will finish all the iteration before, finishing one  iteration of the "inner loop"
rows = int(input("Enter the number for rows :"))
cols = int(input("Enter the number for columns :"))
symbol = input("Enter a symbol :")

for row in range(rows):
    for col in range(cols):
        print(symbol, "", end="")
    print()
