#Nabil 
#Praktikum Algoritma - Program sederhana python

nama = input("Masukkan nama Anda: ")
berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi = float(input("Masukkan tinggi badan Anda (m): "))
bmi = berat / (tinggi ** 2)

print(f"{nama}, skor BMI kamu adalah {bmi}")