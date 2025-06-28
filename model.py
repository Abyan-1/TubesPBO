import datetime

class Transaksi:
    def __init__(self, deskripsi, jumlah, kategori, tanggal, id_transaksi=None):
        self.id = id_transaksi
        self.deskripsi = deskripsi or "Tanpa Deskripsi"
        self.jumlah = float(jumlah) if jumlah and jumlah > 0 else 0.0
        self.kategori = kategori or "Lainnya"
        if isinstance(tanggal, str):
            self.tanggal = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()
        elif isinstance(tanggal, datetime.date):
            self.tanggal = tanggal
        else:
            self.tanggal = datetime.date.today()

    def to_dict(self):
        return {
            "deskripsi": self.deskripsi,
            "jumlah": self.jumlah,
            "kategori": self.kategori,
            "tanggal": self.tanggal.strftime("%Y-%m-%d")
        }
