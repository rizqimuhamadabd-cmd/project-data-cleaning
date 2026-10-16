import pandas as pd
import numpy as np
from pathlib import Path

# 1. Membaca dataset asli
df = pd.read_csv("data/dataset_penjualan_toko_100_baris.csv")

print("JUMLAH DATA SEBELUM CLEANING:", df.shape)

# 2. Menghapus spasi dan menyeragamkan teks
kolom_teks = [
    "nama_produk",
    "kategori",
    "kota_pelanggan",
    "metode_pembayaran"
]

for kolom in kolom_teks:
    df[kolom] = df[kolom].astype("string").str.strip()

df["nama_produk"] = df["nama_produk"].str.title()
df["kategori"] = df["kategori"].str.title()
df["kota_pelanggan"] = df["kota_pelanggan"].str.title()
df["metode_pembayaran"] = df["metode_pembayaran"].str.upper()

# 3. Membersihkan format harga
df["harga_satuan"] = (
    df["harga_satuan"]
    .astype("string")
    .str.replace(r"(?i)rp\s*", "", regex=True)
    .str.replace(".", "", regex=False)
    .str.strip()
)

df["harga_satuan"] = pd.to_numeric(
    df["harga_satuan"], errors="coerce"
)

# 4. Mengubah jumlah menjadi angka
df["jumlah"] = pd.to_numeric(
    df["jumlah"], errors="coerce"
)

# 5. Menyamakan format tanggal
df["tanggal"] = pd.to_datetime(
    df["tanggal"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

# 6. Memeriksa data kosong sebelum penanganan
print("\nDATA KOSONG SEBELUM PENANGANAN:")
print(df.isnull().sum())

# 7. Menangani data kosong
df["jumlah"] = df["jumlah"].fillna(
    df["jumlah"].median()
)

df["harga_satuan"] = df["harga_satuan"].fillna(
    df["harga_satuan"].median()
)

kolom_kategori = [
    "nama_produk",
    "kategori",
    "kota_pelanggan",
    "metode_pembayaran"
]

for kolom in kolom_kategori:
    df[kolom] = df[kolom].fillna("Tidak Diketahui")

# 8. Menghapus transaksi duplikat berdasarkan ID
df = df.drop_duplicates(subset=["id_transaksi"])

# 9. Transformasi: menghitung total penjualan
df["total_penjualan"] = (
    df["jumlah"] * df["harga_satuan"]
)

# Membulatkan jumlah agar menjadi bilangan bulat
df["jumlah"] = df["jumlah"].round().astype(int)

# 10. Menyimpan hasil data bersih
Path("output").mkdir(exist_ok=True)

df.to_csv(
    "output/data_penjualan_bersih.csv",
    index=False,
    encoding="utf-8-sig"
)

# 11. Menampilkan ringkasan hasil
print("\nJUMLAH DATA SETELAH CLEANING:", df.shape)

print("\nDATA KOSONG SETELAH CLEANING:")
print(df.isnull().sum())

print("\nLIMA DATA HASIL CLEANING:")
print(df.head())

print("\nFile tersimpan di output/data_penjualan_bersih.csv")
