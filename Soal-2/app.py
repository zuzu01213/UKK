def cek_tahun_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

# Input tahun dari pengguna
tahun = int(input("Masukkan tahun: "))

# Cek apakah tahun tersebut adalah tahun kabisat atau bukan
if cek_tahun_kabisat(tahun):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")
