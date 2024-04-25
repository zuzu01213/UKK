def sapa():
    print("Halo! Selamat datang di kalkulator sederhana.")

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Tidak bisa dibagi oleh 0"
    else:
        return a / b

# Fungsi untuk meminta input angka dari pengguna
def masukkan_angka():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    return angka1, angka2

# Main program
sapa()

angka1, angka2 = masukkan_angka()

hasil_penjumlahan = penjumlahan(angka1, angka2)
hasil_pengurangan = pengurangan(angka1, angka2)
hasil_perkalian = perkalian(angka1, angka2)
hasil_pembagian = pembagian(angka1, angka2)

print("Hasil penjumlahan:", hasil_penjumlahan)
print("Hasil pengurangan:", hasil_pengurangan)
print("Hasil perkalian:", hasil_perkalian)
print("Hasil pembagian:", hasil_pembagian)
