import pandas as pd
import matplotlib.pyplot as plt

# Membaca data yang sudah dibersihkan
df = pd.read_csv("output/data_penjualan_bersih.csv")

# Menghitung total penjualan berdasarkan kategori
penjualan_kategori = df.groupby("kategori")["total_penjualan"].sum()

# Membuat grafik batang
plt.figure(figsize=(8, 5))
penjualan_kategori.plot(kind="bar")

plt.title("Total Penjualan Berdasarkan Kategori")
plt.xlabel("Kategori Produk")
plt.ylabel("Total Penjualan (Rp)")
plt.xticks(rotation=0)
plt.tight_layout()

# Menyimpan grafik
plt.savefig("output/grafik_penjualan.png")
plt.show()

print("Grafik berhasil dibuat!")
print(penjualan_kategori)
