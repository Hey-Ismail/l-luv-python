# ---------------------#
# //* if, elif, and else statements are used to execute different blocks of code based on the evaluation of conditions,
# //*with if evaluating the initial condition, elif (short for "else if") handling subsequent conditions,
# //*and else covering all remaining cases when previous conditions are not met.
age = int(input("How old are you: "))

if age > 0 and age <= 10:
    print("You are a child!")
elif age < 18:
    print("You are a teenager.")
elif age >= 18 and age <= 25:
    print("You are an adult.")
elif age >= 28 and age < 45:
    print("Are u married(yes/no)")
    command = input("Are you married (yes/no): ").lower()
    if command == "yes":
        print("Congratulations on your marriage.")
    else:
        print("Tell your parents to search for a wife for you!")
elif age >= 45:
    choice = input("Do u have children's(yes/no): ").lower()
    if choice == "yes":
        children = int(input("How many children do you have: "))
        if children >= 1 and children < 4:
            print("You are good to go.")
        else:
            print("Use 'condom', brother!!!")
    else:
        print("set a mode for your wife. ")
elif age == 50:
    print("You are in the middle of your age.")
elif age <= 99:
    print("Stay strong, brother.")
elif age >= 100:
    print("You are a century years old.")
else:
    print("Something went wrong.")
