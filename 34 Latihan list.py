# Program list buku

list_buku = []
while True:
    print("Masukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n","="*20)
    isSelesai = input("Apakah dilanjutkan? (Y/N)")

    if isSelesai == "n" or "N":
        break
