# --------------#
# //* args --> a parameter that will pack all arguments into a tuple(unchanged and immutable)
# //*            useful so that a function can accept a varying amount of arguments.


def calculation(
    *args,
):  # After adding (*) we can write anything and send as much arguments as needed.

    sum = 0
    # args = list(args) # converting args into list
    # args[9] = 0
    for i in args:
        sum += i
    return sum


print("The answer is :", calculation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
