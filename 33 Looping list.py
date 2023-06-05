# Looping dari list

kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

# Loop dan range

kumpulan_angka = [10,4,5,2,6,5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka = {kumpulan_angka[i]}")

# While

print("\nWhile loop")
kumpulan_angka = [10,4,5,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"Angka = {kumpulan_angka[i]}")
    i += 1

# List Comprehension

data = ["Ucup",1,2,3,"Otong"]
[print(f"data={i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
 
# Enumerate
print("\nEnumerate")
data_list = ["Ucup",1,2,3,"Otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")