# --------------#
# //* Nested function calls --> Functions that calls inside other function calls
# //*                            innermost function calls are resolves first
# //*                            returned value is used as argument for the next outer function

# Example-01
number = input("Enter a positive number :")
number = float(number)
number = abs(number)
number = round(number)
print(number)

print("Result :" + str(round(abs(float(input("Enter a positive number :"))))))
# in this line at first the input function was called.
# then it converted the input value into float
# then into absolute value
# then the value will the rounded
# then it will converted into string to print the input value
