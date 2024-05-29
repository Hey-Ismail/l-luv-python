# ------------#
# //*Multi-dimensional lists --> A list of a list , also known as 2D list.
A = [1, 2, 3]
B = [4, 5, 6]
C = [7, 8, 9]

# printing with index
number = [A, B, C]
print(number[0])
print(number[1])
print(number[2])
print(number[1][2], number[2][2])

# Printing with loop
for i in number:
    print(i)
a = [[2, 4, 6, 8], [1, 3, 5, 7], [8, 6, 4, 2], [7, 5, 3, 1]]

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], "", end="")
    print()
