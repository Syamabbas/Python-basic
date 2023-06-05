angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # Aksi 1

    if angka == 3:
        print("Nice")
        continue # Akan membuat loop meloncat ke step selanjutnya

    print("Whatsupp")# Aksi 2

print("Finish!")