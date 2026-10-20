print("=================================")
print("   PROGRAM ARITMATIKA PYTHON")
print("=================================")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\nPilih operasi aritmatika:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (x)")
print("4. Pembagian (:)")

pilihan = input("Masukkan pilihan (1-4): ")

if pilihan == "1":
    hasil = angka1 + angka2
    print("Hasil penjumlahan =", hasil)

elif pilihan == "2":
    hasil = angka1 - angka2
    print("Hasil pengurangan =", hasil)

elif pilihan == "3":
    hasil = angka1 * angka2
    print("Hasil perkalian =", hasil)

elif pilihan == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil pembagian =", hasil)
    else:
        print("Error: Angka tidak boleh dibagi nol!")

else:
    print("Pilihan tidak valid!")

print("=================================")
print("       PROGRAM SELESAI")
print("=================================")
