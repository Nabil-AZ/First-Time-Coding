waktu_parkir= int(input("Berapa jam parkir:"))
if waktu_parkir <= 2:
    biaya= 5000
else:
    tambahan = waktu_parkir - 2
    biaya_tambahan = tambahan * 3000
    biaya = 5000 + biaya_tambahan
print(f"Parkir {waktu_parkir} jam bayar Rp. {biaya}")