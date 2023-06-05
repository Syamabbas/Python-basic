## Operasi

data = ["Ucup","Otong","Dudung"]

data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# info jumlah data dalam list
panjang_data = len(data)

## Manipulasi data list

print(f"Data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"Data sesudah ditambah = \n{data}")

# Menambah diakhir
data.append("Jajang")
print(f"Data ditambah lagi =\n{data}")

# Menambah list dengan list
data_baru = ["Ujang","Usop","Danang"]
data.extend(data_baru)
print(f"Data gabungan = \n{data}")

# Merubah data
data[2] = "Michael"
print(f"data index 2 diubah menjadi = \n{data}")

# Menghilangkan data
data.remove("Ujang")
print(f"Data setelah dihapus = \n{data}")

# Munculkan data terakhir
data_akhir = data.pop()
print(f"Data akhir = \n{data}")

print(data_akhir)