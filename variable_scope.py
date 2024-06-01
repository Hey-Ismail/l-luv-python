# -------------------#
# //* Scope --> The region that a variable is recognized
# //*           a variable is only available for inside region it is created
# //*           a global and locally scoped version of a variable can be created

name = "Ismail Hossain"  # It's a global variable


def display_name():
    name = "Ismail Hossain Fahim"  # It's a local variable
    print(f"Hi,{name}")


display_name()
print(f"Hi,{name}")
