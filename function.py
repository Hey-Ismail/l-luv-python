# -----------------#
# //* Functions --> A block of code which is executed only when it is called.


def greet(name, age):  # This is called parameters(it will be supplied arguments).
    print(f"Assalamu Alaikum,{name}")
    print(f"You are {age} years old")
    print("Stay blessed and have a good day!!!")


name = input("Enter your name\n:")
age = int(input("How old are you ?\n:"))
greet(name, age)  # This is what we send to the function (it is called an argument).
