# Latihan komparasi dan logika

inputUser = float(input("Masukkan nilai kurang dari 3 atau lebih besar dari 10 : \n"))

# Memeriksa angka kurang dari 3
isiKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isiKurangDari)

# Memeriksa angka lebih dari 10
isiLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isiLebihDari)

# Mengecek angka
isCorrect = isiKurangDari or isiLebihDari
print("Angka yang anda masukkan : ", isCorrect)

# -----3++++++++10--------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -----3++++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)

# +++++++++++++++10-------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ",isKurangDari)

# -----3++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)