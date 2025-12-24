# Coffee-Shop-Inventory
Deskripsi

Sistem Manajemen Inventaris Coffee Shop adalah aplikasi berbasis Python yang dirancang untuk membantu pemilik coffee shop mengelola stok barang seperti kopi, bahan tambahan, dan perlengkapan lainnya. Sistem ini menggunakan struktur data sederhana (list of lists) untuk menyimpan data inventaris, tanpa memerlukan database eksternal. Cocok untuk coffee shop kecil hingga menengah yang ingin melacak stok, harga, kategori, dan histori restock secara efisien.

Proyek ini dibangun sebagai contoh implementasi CRUD (Create, Read, Update, Delete) dalam Python, dengan fitur tambahan seperti sorting, searching, laporan, dan restock. Ideal untuk belajar pemrograman Python atau sebagai dasar untuk pengembangan aplikasi inventaris yang lebih kompleks.

Fitur Utama

CRUD Barang: Tambah, tampilkan, update, dan hapus barang (dengan soft delete untuk menjaga data).
Filter dan Tampilan: Tampilkan barang berdasarkan kategori atau semua barang aktif.
Sorting: Urutkan barang berdasarkan nama atau stok.
Searching: Cari barang berdasarkan kode atau nama (case-insensitive).
Laporan: Generate laporan total nilai stok dan daftar barang dengan stok rendah (< 5).
Restock: Tambah stok barang dengan histori tanggal dan jumlah restock.
Menu Interaktif: Antarmuka berbasis terminal untuk navigasi mudah.
Teknologi yang Digunakan

Bahasa Pemrograman: Python 3.x
Struktur Data: List of lists (tanpa library eksternal kecuali datetime untuk histori restock)
Version Control: Git dan GitHub untuk pengembangan kolaboratif
