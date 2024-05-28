# ---------------#
# //* Loop control statement --> change a loop execution form its normal sequence
# //* there are three types of control statement( break, continue and pass)

# Break --> It's used to terminate the loop entirely
guess_the_number = int(input("Guess the correct number(1-100) :"))
target_number = 69

while True:
    if guess_the_number == target_number:
        print(f"you have guess it correctly ")
        break
    else:
        print("Incorrect number , try again")
        guess_the_number = int(input("Guess the correct number(1-100) :"))

# Continue --> It will skip the next iteration of the loop
phone_number = "123-456-789"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# Pass --> dose nothing , acts as a placeholder\
for i in range(10):
    if i == 6:
        pass
    print(i, "", end="")
