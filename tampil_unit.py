import csv
import os
from models import UnitPS

def muat_data():
    daftar_unit = []
    if not os.path.exists("rental_ps.csv"):
        print("File rental_ps.csv tidak ditemukan.")
        return daftar_unit

    with open("rental_ps.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati baris header

        for row in reader:
            unit = UnitPS(
                nama_unit=row[0],
                tipe=row[1],
                tarif_per_jam=row[2],
                status=row[3]
            )
            daftar_unit.append(unit)

    return daftar_unit

def tampilkan_unit():
    daftar_unit = muat_data()
    if not daftar_unit:
        print("Tidak ada data unit PS.")
        return

    print("\n=== DAFTAR UNIT RENTAL PLAYSTATION ===\n")
    print(f"{'Nama Unit':25}{'Tipe':20}{'Tarif/Jam':20}{'Status'}")
    print("-" * 75)
    for unit in daftar_unit:
        print(
            f"{unit.nama_unit:25}"
            f"{unit.tipe:20}"
            f"{'Rp ' + unit.tarif_per_jam:20}"
            f"{unit.status}"
        )
    print("-" * 75)
    print(f"Total Unit: {len(daftar_unit)}")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Unit")
        print("2. Refresh Data")
        print("0. Keluar")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            tampilkan_unit()
        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_unit()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()