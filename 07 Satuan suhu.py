# Latihan konversi satuan suhu

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# Celcius
celcius = float(input('Masukkan suhu dalam celcius : '))
print("Suhu adalah ",celcius, "celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit,"Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ",kelvin, "Kelvin")