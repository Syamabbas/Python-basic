# Latihan membuat segitiga

sisi = 10

# 1. Memakai for

print("Awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir dari for ")

# 2. Menggunakan while

print("Awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir while")

# 3. Hanya ganjil

print("Awal while")
while True:
    if (count%2):
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir while")
