import subprocess

def buka_tambah_unit():
    subprocess.run(["python", "tambah_unit.py"])

def buka_tampil_unit():
    subprocess.run(["python", "tampil_unit.py"])

def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM RENTAL PLAYSTATION ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Unit PS")
        print("2. Tampilkan Unit PS")
        print("0. Keluar")
        print("=" * 40)
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            buka_tambah_unit()
        elif pilihan == "2":
            buka_tampil_unit()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()