# ----------------#
# //* Exception --> Events detected during that interrupt the flow of a program

# This is cause an run time error.
# numerator = int(input("Enter a number :"))
# denominator = int(input("Enter another number :"))
# result = numerator / denominator
# print(result)

# else we can try this to handle errors
try:
    numerator = int(input("Enter a number :"))
    denominator = int(input("Enter another number :"))
    result = numerator / denominator


except ZeroDivisionError:
    print("You can't divided by zero")

except ValueError:
    print("input is not matched.pls give numerical value")

else:
    print(result)

finally:
    print("This line will execute")
# except Exception as e:
#     print(e)
# except Exception:
#     print("This is handle all type of errors")
