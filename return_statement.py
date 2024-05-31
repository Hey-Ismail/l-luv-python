# --------------#
# //* Return Statement --> the functions send the values/ objects back to the caller
# //*                         these vales/objects are knowns as the function's return statement


def calculate(x, y, user_choice):
    if user_choice == "+":
        return x + y
    elif user_choice == "-":
        return x - y
    elif user_choice == "*":
        return x * y
    elif user_choice == "/":
        return x / y
    elif user_choice == "//":
        return x // y
    elif user_choice == "%":
        return x % y
    else:
        return "Choose the correct operator"


x = int(input("Enter the first value :"))

print("Choose an operator from the following chart.")
print(
    """
Addition --> '+'
Subtraction --> '-'
Multiplication --> '*'
Division --> '/'
Floor Division --> '//'
Modulus --> '%'
"""
)
user_choice = input("Which operator you want to choose :")

y = int(input("Enter the second value :"))

result = calculate(x, y, user_choice)
print(f"The result is : {result}")
