# Store Management CLI

---

# Tech Stack

## Programming Language
- Python

---

## External Library
- Matplotlib
- rich

---

## Built-in Python Library
- datetime
- os
- path
- csv

---

# Application Type

- CLI (Command Line Interface)
- Offline Application
- Local Storage
- Single User

---

# Main Feature

## 1. Management Product
## 2. Management Promotion
## 3. Management Transaction
## 4. Store Statistic

---

# Menu 1 - Product Management

- Menambahkan data barang
- Menampilkan seluruh informasi barang yang tersedia Total product
- Mencari barang berdasarkan SKU
- Mengupdate barang:
  - Update nama barang
  - Update harga barang
  - Update stock barang
  - Update seluruh data barang
- Menghapus barang berdasarkan SKU

---

# Menu 2 - Promotion Management

- Menambahkan diskon product
  - Input SKU product yang akan di diskon
  - Input persentase diskon
- Menghapus diskon product
- Melihat seluruh product yang sedang diskon
  - Menampilkan harga asli dan harga setelah diskon
- cari product yang sedang diskon berdasarkan SKU atau nama barang 
- update informasi barang yang sedang diskon 
---

# Menu 3 - Transaksi management

- Penjualan
- Melihat transaksi masuk dan keluar serta total transaksi
- Mengecek saldo store
- unduh laporan keuangan csv


---

# menu 4 - Store analytik
- Menampilkan product paling laku
- menamplkan penjualan product diskon 
- Menampilkan product dengan stock hampir habis dan yang tersisa
- Menampilkan grafik omset penjualan menggunakan matplotlib






# Data Structure
## Product Data

```python
{
    "sku": "P001",
    "name": "Keyboard",
    "price": 150000,
    "stock": 10,
    "discount": 0
}