data_0 = [1,2]
data_1 = [3,4,5]

data_list = [1,2,3,4]

print(f"List biasa = {data_list}")

list_2D = [data_0,data_1,6,7]

print(f"List 2D = {list_2D}")

# Contoh penggunaan

peserta_0 = ["Ucup",25,"Laki-laki"]
peserta_1 = ["Otong",10,"Laki-laki"]
peserta_2 = ["Dedeh",50,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"Peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")
