# -------------#
# //* Keyword argument --> An argument preceded by an identifier when we pass them to a function
# //*                      The order of the argument doesn't matter , unlike the positional argument
# //*                      python knows the names of the argument that user function receives.


def greet(first_name, middle_name, last_name):
    print(f"You first name is :{first_name}")
    print(f"Your middle name is :{middle_name}")
    print(f"Your last name is :{last_name}\n")
    print(f"Assalamu alaikum, {first_name} {middle_name} {last_name}")


# first_name =input("Enter your first name :")
# middle_name =input("Enter your middle name :")
# last_name =input("Enter your last name :")

greet(middle_name="Hossain", last_name="Fahim", first_name="Ismail")
