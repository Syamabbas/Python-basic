data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
data_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_copy}")

# Mengambil data daro nested list

data = data_2D[1][0]
print(f"Data = {data}")

# Deep copy

from copy import deepcopy

data_deepcopy = deepcopy(data_2D)

print(f"Address asli = {hex(id(data_2D))}")
print(f"Address deep = {hex(id(data_deepcopy))}")

print("Address Member 1")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address deep = {hex(id(data_deepcopy[0]))}")
