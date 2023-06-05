## Teknik menduplikat list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# Menduplikat dengan copy

print("Membuat list C dengan a copy")
c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Mengubah data di C
print("Kita ubah data C")
c[0] = "Danang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Mengubah data di A
print("Kita ubah data A")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")