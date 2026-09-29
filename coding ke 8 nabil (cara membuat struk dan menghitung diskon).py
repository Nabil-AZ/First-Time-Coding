print("--- program perhitungan diskonan pembelanjaan USAKTIF---")
print()
Nama = input("Masukkan Nama: ")
Nim = int(input("Masukkan NIM: "))
Total_belanja = int(input("Masukkan total belanja: "))
Kupon = input("Masukkan kode kupon: ")
Persen_diskon = 100

if Kupon == "IKL6309": 
    Diskon = Total_belanja *(Persen_diskon / 100)
    Total_bayar = Total_belanja - Diskon
    print("Selamat, Anda mendapatkan diskon 100%")
    print()
    print("Nama: ", Nama)
    print("NIM: ", Nim)
    print("Total belanja: ", Total_belanja)
    print("Diskon: ", Diskon)
    print("Total bayar: ", Total_bayar)

elif Total_belanja >= 40000 and Total_belanja < 89999:
    Diskon = Total_belanja * 0.20
    Total_bayar = Total_belanja - Diskon
    print("Selamat, Anda mendapatkan diskon 20%")
    print()
    print("Nama: ", Nama)
    print("NIM: ", Nim)
    print("Total belanja: ", Total_belanja)
    print("Diskon: ", Diskon)
    print("Total bayar: ", Total_bayar)

elif Total_belanja >= 90000 and Total_belanja < 189999:
    Diskon = Total_belanja * 0.40
    Total_bayar = Total_belanja - Diskon
    print("Selamat, Anda mendapatkan diskon 40%")
    print()
    print("Nama: ", Nama)
    print("NIM: ", Nim)
    print("Total belanja: ", Total_belanja)
    print("Diskon: ", Diskon)
    print("Total bayar: ", Total_bayar)

elif Total_belanja >= 190000 and Total_belanja < 389999:
    Diskon = Total_belanja * 0.60
    Total_bayar = Total_belanja - Diskon
    print("Selamat, Anda mendapatkan diskon 60%")
    print()
    print("Nama: ", Nama)
    print("NIM: ", Nim)
    print("Total belanja: ", Total_belanja)
    print("Diskon: ", Diskon)
    print("Total bayar: ", Total_bayar)

elif Total_belanja >= 390000:
    Diskon = Total_belanja * 0.80
    Total_bayar = Total_belanja - Diskon
    print("Selamat, Anda mendapatkan diskon 80%")
    print()
    print("Nama: ", Nama)
    print("NIM: ", Nim)
    print("Total belanja: ", Total_belanja)
    print("Diskon: ", Diskon)
    print("Total bayar: ", Total_bayar)