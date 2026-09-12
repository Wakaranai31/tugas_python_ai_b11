def greet(nama: str) -> str:
    return "Halo, " + nama + "!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    
    total = sum(angka)
    hasil = total / len(angka)
    return round(hasil, 2)


class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self) -> str:
        rata = self.rata_nilai()
        stat = self.status()
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={rata}, status={stat})"


if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print("greet('Arifian'):", greet("Arifian"))
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))
    print()

    print("=== CLASS STUDENT ===")
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80.5)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(77.0)
    
    print(mhs1)
    print("Rata-rata nilai Budi:", mhs1.rata_nilai())
    print("Status kelulusan Budi:", mhs1.status())
    print()

    mhs2 = Student("Citra", "B456")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(55.5)
    mhs2.tambah_nilai(65.0)
    
    print(mhs2)
    print("Rata-rata nilai Citra:", mhs2.rata_nilai())
    print("Status kelulusan Citra:", mhs2.status())
