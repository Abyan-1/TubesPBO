import streamlit as st
from model import Transaksi
from manajer_transaksi import ManajerTransaksi
from konfigurasi import KATEGORI_TRANSAKSI
import datetime
import pandas as pd

manager = ManajerTransaksi()
st.title("Manchester United : Tracker Donasi & Merchandise Klub")

menu = st.sidebar.radio("Menu", ["Tambah Transaksi", "Riwayat", "Ringkasan"])

if menu == "Tambah Transaksi":
    st.header("Form Transaksi")
    with st.form("form_transaksi"):
        deskripsi = st.text_input("Deskripsi")
        jumlah = st.number_input("Jumlah (Euro)", min_value=0.1)
        kategori = st.selectbox("Kategori", KATEGORI_TRANSAKSI)
        tanggal = st.date_input("Tanggal", value=datetime.date.today())
        submit = st.form_submit_button("Simpan")

        if submit:
            transaksi = Transaksi(deskripsi, jumlah, kategori, tanggal)
            manager.tambah_transaksi(transaksi)
            st.success("Transaksi berhasil dicatat!")

elif menu == "Riwayat":
    st.header("Riwayat Transaksi")
    data = manager.ambil_semua()
    if not data:
        st.info("Belum ada transaksi.")
    else:
        data_dict = []
        for t in data:
            d = t.to_dict()
            d["ID"] = t.id   # ← Ambil ID asli dari database
            data_dict.append(d)

        df = pd.DataFrame(data_dict)
        df = df[["ID", "tanggal", "kategori", "deskripsi", "jumlah"]]  # urutkan kolom agar ID di awal
        df = df.rename(columns={"tanggal": "Tanggal", "kategori": "Kategori", "deskripsi": "Deskripsi", "jumlah": "Jumlah (Rp)"})

        st.dataframe(df, use_container_width=True)


        id_hapus = st.number_input("Masukkan ID transaksi yang ingin dihapus", min_value=1, step=1)

        if st.button("Hapus Transaksi"):
            manager.hapus_transaksi(id_hapus)
            st.success(f"Transaksi dengan ID {id_hapus} berhasil dihapus.")
            st.rerun()


elif menu == "Ringkasan":
    st.header("Ringkasan")
    total = manager.total_pemasukan()
    st.metric("Total Dana Masuk", f"Rp {total:,.0f}")
    perkat = manager.per_kategori()
    if perkat:
        df_kat = pd.DataFrame({
            "Kategori": perkat.keys(),
            "Jumlah": perkat.values()
        })
        st.bar_chart(df_kat.set_index("Kategori"))
    else:
        st.info("Belum ada data.")
