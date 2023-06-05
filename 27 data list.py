# Membuat list

data_range = list(range(0,10,3)) # Start, stop, step
print(data_range)

# Membuat list dengan for loop, list comprehension
data_list_for = [i**2 for i in range(0,10)] # pangkat
print(data_list_for)

# Membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

# Membuat list genap
list_for_genap = [i for i in range(0,10) if i%2 == 0]
print("List genap :\n",list_for_genap)

# Membuat list ganjil
list_ganjil = [i for i in range(0,10) if i%2 != 0]
print("List ganjil :\n",list_ganjil)