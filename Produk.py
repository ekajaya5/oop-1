class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk: {self.nama}")
        print(f"Harga: Rp{self.harga:,}")

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon_dan_bayar(self, jumlah, total_semua):
        if total_semua > 5000:
            diskon = total_semua * 15 / 100
            bayar = total_semua - diskon
            return diskon, bayar
        else:
            return 0, total_semua