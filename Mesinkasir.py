
keranjang = []

def menu():
    print("Mesin Kasir Sederhana")
    print("1. Lihat stok")
    print("2. Tambah item ke keranjang")
    print("3. Lihat keranjang")
    print("4. Total belanja")
    print("5. Pembayaran")
    print("6. Keluar")

stok = [
    {"nama": "Beras", "harga": 10000, "jumlah": 50},
    {"nama": "Minyak Goreng", "harga": 15000, "jumlah": 30},
    {"nama": "Gula", "harga": 12000, "jumlah": 40},
    {"nama": "Garam", "harga": 5000, "jumlah": 100},
]


def lihat_stok():
    print("===== Stok Barang =====")
    if not stok:
        print("Stok barang kosong.")
    else:
        for item in stok:
            print(f"{item['nama']} - Rp {item['harga']} - {item['jumlah']} unit")

def masukkan_barang_keranjang():
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Jumlah barang: "))

    for item in stok:
        if item['nama'] == nama: #pemeriksaan barang 
            if item['jumlah'] >= jumlah:
                item['jumlah'] -= jumlah
                barang = {"nama": nama, "harga": item['harga'], "jumlah": jumlah}
                keranjang.append(barang)
                print(f"{jumlah} unit {nama} telah ditambahkan ke keranjang.")
                if item['jumlah'] == 0:
                    stok.remove(item)
                break #keluar 
            else:
                print(f"Stok {nama} tidak mencukupi. Tersedia: {item['jumlah']} unit.")
                break
    else:
        print(f"Barang {nama} tidak ditemukan di stok.")




def lihat_keranjang():
    print("===== Keranjang Belanja =====")
    if not keranjang:
        print("Keranjang belanja kosong.")
    else:
        for item in keranjang:
            total_item = item['harga'] * item['jumlah']
            print(f"{item['nama']} - {item['jumlah']} x Rp {item['harga']} = Rp {total_item}")

def total_belanja():
    total = sum(item['harga'] * item['jumlah'] for item in keranjang)
    print(f"Total belanja: Rp {total}")
    return total

def pembayaran():
    total = total_belanja()
    uang_dibayar = int(input("Masukkan uang yang dibayar: Rp "))
    if uang_dibayar >= total:
        kembalian = uang_dibayar - total
        print(f"Uang yang dibayar: Rp {uang_dibayar}")
        print(f"Kembalian: Rp {kembalian}")
    else:
        kekurangan = total - uang_dibayar
        print(f"Uang yang dibayar kurang Rp {kekurangan}")

def main():
    while True:
        menu()
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            lihat_stok()
        elif pilihan == '2':
            masukkan_barang_keranjang()
        elif pilihan == '3':
            lihat_keranjang()
        elif pilihan == '4':
            total_belanja()
        elif pilihan == '5':
            pembayaran()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan mesin kasir sederhana.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()

