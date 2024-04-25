def hitung_gaji_mingguan(nama, golongan, jam_kerja):
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        return "Golongan tidak valid"

    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0

    gaji_mingguan = (upah_per_jam * jam_kerja) + uang_lembur
    return nama, gaji_mingguan

# Input data karyawan dari pengguna
nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan karyawan (A/B/C/D): ").upper()
jam_kerja = float(input("Masukkan jumlah jam kerja per minggu: "))

# Hitung gaji mingguan menggunakan fungsi yang telah dibuat
nama_karyawan, gaji = hitung_gaji_mingguan(nama, golongan, jam_kerja)

# Tampilkan hasil
print(f"Pegawai {nama_karyawan} menerima gaji sebesar: {gaji}")
