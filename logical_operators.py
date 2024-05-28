# ------------#
# //* Logical operators (and,or,not) --> used to check if two or more conditional statement is true.


# and operator
temp = int(input("What is the temperature outside today? :"))
if temp > 0 and temp < 32:
    print(f"Crisp, {temp}, degrees! Enjoy the fresh air.")
else:
    print("try again.")

# or operator
temp = int(input("What is the temperature outside today? :"))
if temp < 0 or temp <= 15:
    print("Brr, it's freezing! Bundle up warmly.")
else:
    print("try again.")

# not operator
temp = int(input("What is the temperature outside today? :"))

if not (temp > 0 and temp <= 32):
    print(f"Crisp, {temp}, degrees! Enjoy the fresh air.")
elif not (temp > 32 and temp >= 20):
    print(f"Brr, it's freezing! Bundle up warmly.")
else:
    print("try again.")
