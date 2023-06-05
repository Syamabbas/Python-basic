data_list = ['Ucup','Otong','Dudung']

print(data_list[0])


data_dict = {
    'cup':'Ucup',
    'tg':'otong',
    'dg':'Dudung',
    'nmbr':100,
    'list':data_list
}

# Panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary: {LENDICT}")

# Mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengecek value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","Key tidak ditemukan"))

# Mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "Asep kaysper"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"sym":"Syam data baru"})
print(data_dict)

# Mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)