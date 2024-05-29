# ------------#
# //* tuple --> A collection which is ordered and unchangeable
# //* used to group together related data
# //* It should surrounded be with parenthesis

cars = ("mercedes-benz", "BMW", "porsche", "mclaren", "Audi")
print(cars.count("porsche"))
print(cars.index("mercedes-benz"))

for i in cars:
    print(i, "", end="")

if "porsche" in cars:
    print("Porsche is here")
