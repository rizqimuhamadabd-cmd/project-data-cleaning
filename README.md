
# Project Data Cleaning dan Transformation

## Deskripsi
Project ini dibuat untuk melakukan proses Data Cleaning dan Transformation pada dataset penjualan toko menggunakan Python.

## Tujuan
- Mengidentifikasi data kosong dan data duplikat.
- Membersihkan format data yang tidak konsisten.
- Mengubah tipe data agar sesuai.
- Menghitung total penjualan setiap transaksi.
- Membuat visualisasi total penjualan berdasarkan kategori produk.

## Dataset
Dataset berisi 100 baris data transaksi penjualan dengan 8 kolom:
- id_transaksi
- tanggal
- nama_produk
- kategori
- jumlah
- harga_satuan
- kota_pelanggan
- metode_pembayaran

Dataset ini merupakan data contoh yang dibuat untuk keperluan pembelajaran.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Visual Studio Code

## Proses Data Cleaning
1. Memeriksa informasi dataset dan nilai kosong.
2. Menghapus spasi berlebih dan menyeragamkan teks.
3. Mengubah format harga dan tanggal.
4. Menangani nilai kosong menggunakan median atau label pengganti.
5. Menghapus transaksi duplikat berdasarkan ID transaksi.

## Proses Transformation
Menambahkan kolom total_penjualan dengan rumus:

total_penjualan = jumlah * harga_satuan

## Visualisasi
Grafik batang digunakan untuk membandingkan total penjualan berdasarkan kategori produk.

## Hasil
Dataset awal berisi 100 baris dan 8 kolom.
Setelah proses cleaning, dataset berisi 97 baris dan 9 kolom.

File hasil cleaning disimpan di folder output.
Grafik penjualan disimpan di folder output.
