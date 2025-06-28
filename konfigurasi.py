import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NAMA_DB = 'transaksi.db'
DB_PATH = os.path.join(BASE_DIR, NAMA_DB)

KATEGORI_TRANSAKSI = [
    "Donasi", "Jersey", "Syal", "Tiket Pertandingan", "Aksesoris"
]
KATEGORI_DEFAULT = "Lainnya"
