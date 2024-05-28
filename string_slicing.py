# -----------------#
# //* slicing --> it creates a substring by tramming elements from another string
# //* there are two type of slicing string
# //* indexing([start:end:step]) and slice([start:end])

# indexing([start:end:step])
my_name = "Ismail Hossain Fahim"
print(f"First name is --> {my_name[0:6]}")
print(f"Middle name is --> {my_name[7:-5]}")
print(f"Sure name is --> {my_name[14:]}")
print(f"Every one knows me as -->{my_name[:14]}")
print(f"My mom calls me --> {my_name[14:]}")
print(f"funky name -->{my_name[0:20:2]}")
print(f"Reversing my name -->{my_name[::-1]}")

# slicing string
my_name = "Ismail Hossain Fahim"
print(my_name[(slice(0, 6))])
print(my_name[(slice(0, 20))])
print(my_name[(slice(7, -6))])
