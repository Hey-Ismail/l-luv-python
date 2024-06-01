# ---------#
# //* **kwargs --> A parameters that wil packed all the arguments into a dictionary
# //*               useful so that a function can accept a varying amount of keyword arguments


def greet(
    **kwargs,
):  # After adding (*) we can write anything and send as much arguments as needed.
    # print(f"Hello ,{kwargs['first_name'],kwargs['middle_name'],kwargs['last_name']}")
    for key, values in kwargs.items():
        print(values, "", end="")


first_name = input("Enter your first name \n-->")
middle_name = input("Enter your middle name \n-->")
last_name = input("Enter your last name \n-->")

greet(first_name=first_name, middle_name=middle_name, last_name=last_name)
