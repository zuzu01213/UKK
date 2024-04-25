def luas_segitiga(alas, tinggi):
    # Rumus luas segitiga: 0.5 * alas * tinggi
    luas = 0.5 * alas * tinggi
    return luas

# Input alas dan tinggi dari pengguna
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Hitung luas segitiga menggunakan fungsi yang telah dibuat
luas = luas_segitiga(alas, tinggi)

# Tampilkan hasil
print("Luas segitiga adalah:", luas)
