class UnitPS:
    def __init__(self, nama_unit, tipe, tarif_per_jam, status="Tersedia"):
        self.nama_unit = nama_unit
        self.tipe = tipe
        self.tarif_per_jam = tarif_per_jam
        self.status = status

    def to_list(self):
        return [self.nama_unit, self.tipe, self.tarif_per_jam, self.status]

    def __str__(self):
        return f"{self.nama_unit} ({self.tipe}) - Rp{self.tarif_per_jam}/jam - {self.status}"


class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp):
        self.id = id_pelanggan
        self.nama = nama
        self.no_hp = no_hp

    def to_list(self):
        return [self.id, self.nama, self.no_hp]

    def __str__(self):
        return f"{self.nama} ({self.id}) - {self.no_hp}"