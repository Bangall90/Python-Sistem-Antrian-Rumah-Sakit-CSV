# Python-Sistem-Antrian-Rumah-Sakit-CSV

TUGAS FINAL PROJECT STRUKTUR DATA  
NAMA : MUHAMMAD YUSUF ALI  
NIM : 25416255201034

Sistem Antrian Rumah Sakit merupakan aplikasi berbasis Python yang digunakan untuk mengelola data pasien dan antrian pelayanan rumah sakit menggunakan database flat file (.CSV). Aplikasi ini dibuat untuk memenuhi tugas Final Project Struktur Data dengan menerapkan konsep struktur data, algoritma pencarian, pengurutan, serta operasi CRUD (Create, Read, Update, Delete). Setiap perubahan data akan langsung tersimpan pada file CSV dan dapat dibaca kembali saat aplikasi dijalankan.

TUJUAN PROYEK
1. Mengimplementasikan operasi CRUD pada data pasien.
2. Menggunakan struktur data Queue untuk mengelola antrian pasien.
3. Menggunakan Hash Map (Dictionary) untuk mempercepat proses pencarian data pasien.
4. Mengimplementasikan algoritma Sorting dan Searching.
5. Menggunakan file CSV sebagai media penyimpanan data.

FITUR UTAMA
1. Tambah Pasien (Create)  
Menambahkan data pasien baru ke dalam sistem dan menyimpannya ke file CSV.  
2. Lihat Data Pasien (Read)  
Menampilkan seluruh data pasien yang tersimpan pada sistem.  
3. Cari Pasien (Searching)  
Mencari pasien berdasarkan ID menggunakan Hash Map (Dictionary) sehingga proses pencarian lebih cepat.  
4. Update Data Pasien (Update)  
Mengubah informasi pasien yang sudah tersimpan.  
5. Hapus Data Pasien (Delete)  
Menghapus data pasien berdasarkan ID.  
6. Panggil Pasien Berikutnya  
Menggunakan Queue untuk memanggil pasien pertama yang masih berstatus Menunggu.  
7. Sorting Data  
Mengurutkan data pasien berdasarkan nama pasien menggunakan fungsi sorting.  

STRUKTUR DATA YANG DIGUNAKAN
1. Queue  
Queue digunakan untuk mengelola urutan pasien yang menunggu pelayanan.  
Prinsip kerja:  
Enqueue = Menambahkan pasien ke antrian.  
Dequeue = Memanggil pasien berikutnya.  

2. Hash Map (Dictionary)  
Hash Map digunakan untuk menyimpan pasangan key-value berupa:  
{
    "P001": data_pasien
}  
Keuntungan:  
Pencarian data lebih cepat dibandingkan pencarian linear.  

ALGORITMA YANG DIGUNAKAN:  
1. Searching  
Pencarian pasien berdasarkan ID menggunakan Dictionary.  

2. Sorting  
Pengurutan data pasien berdasarkan nama menggunakan fungsi sorted().  

MENU PROGRAM  
1. Tambah Pasien
2. Tampilkan Data Pasien
3. Cari Pasien
4. Update Pasien
5. Hapus Pasien
6. Panggil Pasien Berikutnya
7. Keluar
