angka_1 = float(input("Masukkan angka 1 = "))
operator = input("Masukkan operator (+,-,*,/) = ")
angka_2 = float(input("Masukkan angka 2 = "))

# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "x" or "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Masukkan dengan benar")

print("Akhir program")