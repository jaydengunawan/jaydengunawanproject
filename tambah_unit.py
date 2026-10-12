import csv
import os
from models import UnitPS

def simpan_unit():
    print("\n=== TAMBAH DATA UNIT PS ===")
    nama_unit = input("Nama Unit     : ").strip()      # Contoh: Unit PS 01
    tipe = input("Tipe Konsol   : ").strip()           # Contoh: PlayStation 5
    tarif = input("Tarif/Jam (Rp): ").strip()           # Contoh: 15000

    if not nama_unit or not tipe or not tarif:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    unit = UnitPS(nama_unit, tipe, tarif)
    file_exists = os.path.exists("rental_ps.csv")

    with open("rental_ps.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nama Unit", "Tipe", "Tarif/Jam", "Status"])
        writer.writerow(unit.to_list())

    print("\n[BERHASIL] Unit PS berhasil ditambahkan.\n")

def main():
    while True:
        print("=== MENU TAMBAH UNIT PS ===")
        print("1. Tambah Unit")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            simpan_unit()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()