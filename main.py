from Produk import Produk

print("DATA PRODUK")

nama1 = input("Nama produk 1: ")
harga1 = int(input("Harga produk 1: "))
jumlah1 = int(input("Jumlah beli: "))

nama2 = input("\nNama produk 2: ")
harga2 = int(input("Harga produk 2: "))
jumlah2 = int(input("Jumlah beli: "))

produk1 = Produk(nama1, harga1)
produk2 = Produk(nama2, harga2)

print("\nINFORMASI PRODUK")
produk1.tampilkan_info()
produk2.tampilkan_info()

total1 = produk1.hitung_total(jumlah1)
total2 = produk2.hitung_total(jumlah2)

print(f"\nTotal {nama1} ({jumlah1} buah): Rp{total1:,}")
print(f"Total {nama2} ({jumlah2} buah): Rp{total2:,}")

total_semua = total1 + total2
diskon, total_bayar = produk1.hitung_diskon_dan_bayar(jumlah1, total_semua)

print(f"\nTotal Pembelian: Rp{total_semua:,}")
print(f"Diskon (15%):    Rp{diskon:,}")
print(f"Total Bayar:     Rp{total_bayar:,}")