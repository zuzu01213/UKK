def hitung_rata_rata(nilai):
    total = sum(nilai)
    rata_rata = total / len(nilai)
    return rata_rata

def masukkan_nilai():
    n = int(input("Masukkan jumlah nilai yang ingin diratakan: "))
    nilai = []
    for i in range(1, n+1):
        nilai.append(float(input(f"Masukkan nilai ke-{i}: ")))
    return nilai

def main():
    print("Program menghitung rata-rata dari sejumlah nilai.")
    nilai = masukkan_nilai()
    rata_rata = hitung_rata_rata(nilai)
    print("Nilai-nilai yang dimasukkan:", nilai)
    print("Rata-rata dari nilai-nilai tersebut adalah:", rata_rata)

if __name__ == "__main__":
    main()
