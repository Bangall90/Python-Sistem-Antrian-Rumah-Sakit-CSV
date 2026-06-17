import csv
import os

FILE_CSV = "pasien.csv"

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def buat_file_jika_belum_ada():
    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nama", "umur", "keluhan", "prioritas", "status"])

def load_data():
    data = []
    buat_file_jika_belum_ada()

    with open(FILE_CSV, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data

def simpan_data(data):
    with open(FILE_CSV, "w", newline="") as file:
        fieldnames = ["id", "nama", "umur", "keluhan", "prioritas", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

def tampilkan_data(data):
    if len(data) == 0:
        print("Data pasien masih kosong.")
        return

    data_sorted = sorted(data, key=lambda x: x["nama"])

    print("\n=== DATA PASIEN ===")
    for pasien in data_sorted:
        print(
            f"ID: {pasien['id']} | "
            f"Nama: {pasien['nama']} | "
            f"Umur: {pasien['umur']} | "
            f"Keluhan: {pasien['keluhan']} | "
            f"Prioritas: {pasien['prioritas']} | "
            f"Status: {pasien['status']}"
        )

def tambah_pasien(data):
    print("\n=== TAMBAH PASIEN ===")
    id_pasien = input("ID Pasien: ")

    hash_map = {pasien["id"]: pasien for pasien in data}

    if id_pasien in hash_map:
        print("ID pasien sudah ada!")
        return

    nama = input("Nama: ")
    umur = input("Umur: ")
    keluhan = input("Keluhan: ")
    prioritas = input("Prioritas Normal/Darurat: ")

    pasien_baru = {
        "id": id_pasien,
        "nama": nama,
        "umur": umur,
        "keluhan": keluhan,
        "prioritas": prioritas,
        "status": "Menunggu"
    }

    data.append(pasien_baru)
    simpan_data(data)
    print("Pasien berhasil ditambahkan.")

def cari_pasien(data):
    print("\n=== CARI PASIEN ===")
    id_pasien = input("Masukkan ID pasien: ")

    hash_map = {pasien["id"]: pasien for pasien in data}

    if id_pasien in hash_map:
        pasien = hash_map[id_pasien]
        print("Data ditemukan:")
        print(pasien)
    else:
        print("Pasien tidak ditemukan.")

def update_pasien(data):
    print("\n=== UPDATE PASIEN ===")
    id_pasien = input("Masukkan ID pasien: ")

    for pasien in data:
        if pasien["id"] == id_pasien:
            pasien["nama"] = input("Nama baru: ")
            pasien["umur"] = input("Umur baru: ")
            pasien["keluhan"] = input("Keluhan baru: ")
            pasien["prioritas"] = input("Prioritas baru Normal/Darurat: ")
            pasien["status"] = input("Status baru: ")

            simpan_data(data)
            print("Data pasien berhasil diupdate.")
            return

    print("Pasien tidak ditemukan.")

def hapus_pasien(data):
    print("\n=== HAPUS PASIEN ===")
    id_pasien = input("Masukkan ID pasien: ")

    for pasien in data:
        if pasien["id"] == id_pasien:
            data.remove(pasien)
            simpan_data(data)
            print("Data pasien berhasil dihapus.")
            return

    print("Pasien tidak ditemukan.")

def panggil_pasien(data):
    print("\n=== PANGGIL PASIEN ===")

    queue = Queue()

    for pasien in data:
        if pasien["status"].lower() == "menunggu":
            queue.enqueue(pasien)

    if queue.is_empty():
        print("Tidak ada pasien dalam antrian.")
        return

    pasien_dipanggil = queue.dequeue()
    pasien_dipanggil["status"] = "Dipanggil"

    simpan_data(data)

    print("Pasien berikutnya dipanggil:")
    print(pasien_dipanggil)

def menu():
    while True:
        data = load_data()

        print("\n=== SISTEM ANTRIAN RUMAH SAKIT ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Data Pasien")
        print("3. Cari Pasien")
        print("4. Update Pasien")
        print("5. Hapus Pasien")
        print("6. Panggil Pasien Berikutnya")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pasien(data)
        elif pilihan == "2":
            tampilkan_data(data)
        elif pilihan == "3":
            cari_pasien(data)
        elif pilihan == "4":
            update_pasien(data)
        elif pilihan == "5":
            hapus_pasien(data)
        elif pilihan == "6":
            panggil_pasien(data)
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
menu()