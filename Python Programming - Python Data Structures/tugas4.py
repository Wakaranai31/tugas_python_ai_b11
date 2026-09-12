print("===========================================")
print("\n--- 1. List ---")

list_campur = [10, "Python", 3.14, True, "AI", 2026]
print("List awal: ", list_campur)
print("Elemen pertama: ", list_campur[0])
print("Elemen terakhir: ", list_campur[5])
print("Elemen start : stop : step ", list_campur[1:5:3])

list_campur.append("Baru")
print("Setelah append: ", list_campur)

list_campur.insert(2, "Sisipan")
print("Setelah insert: ", list_campur)

list_campur.extend([99, 100])
print("Setelah extend: ", list_campur)

dibuang = list_campur.pop()
print("Setelah pop (buang", dibuang, "): ", list_campur)

list_campur.remove("AI")
print("Setelah remove Python: ", list_campur)
print("\n===========================================")


print("===========================================")
print("\n--- 2. Tuple ---")

angka_tuple = (10, 20, 30, 40, 50, 60)
print("Tuple awal:", angka_tuple)
print("Panjang tuple:", len(angka_tuple))
print("Akses indeks ke-2:", angka_tuple[2])

a, b, *sisanya = angka_tuple
print("Unpacking: a =", a, "b =", b, "sisanya =", sisanya)
print("\n===========================================")


print("===========================================")
print("\n--- 3. Set ---")

himpunan1 = {1, 2, 3, 4, 5}
himpunan2 = {4, 5, 6, 7, 8}

print("Set 1:", himpunan1)
print("Set 2:", himpunan2)
print("Union:", himpunan1 | himpunan2)
print("Intersection:", himpunan1 & himpunan2)
print("Difference:", himpunan1 - himpunan2)
print("Symmetric Difference:", himpunan1 ^ himpunan2)
set_duplikat = {1, 1, 2, 2, 3, 3, 3}
print("Tes duplikat hilang otomatis:", set_duplikat)
print("\n===========================================")


print("===========================================")
print("\n--- 4. Dictionary ---")

mahasiswa = {
    "nama": "Budi Santoso",
    "nim": "12345678",
    "angkatan": 2023,
    "kota": "Jakarta"
}
print("Dictionary awal:", mahasiswa)

mahasiswa["jurusan"] = "Informatika"  
mahasiswa["kota"] = "Bandung"         
del mahasiswa["angkatan"]             

print("\nSetelah dimodifikasi:", mahasiswa)

print("\nKeys:", mahasiswa.keys())

print("\nValues:", mahasiswa.values())

print("\nItems:", mahasiswa.items())

print("\nIterasi key dan value:")

for k, v in mahasiswa.items():
    print(k, ":", v)
print("\n===========================================")


print("===========================================")
print("\n--- 5. Nested Structures ---")
daftar_buku = [
    {"judul": "Belajar Python", "penulis": "Andi", "tahun": 2026},
    {"judul": "Machine Learning", "penulis": "Budi", "tahun": 2025},
    {"judul": "Data Science", "penulis": "Citra", "tahun": 2024},
    {"judul": "AI", "penulis": "Dina", "tahun": 2023}
]

print("Judul buku:")
for b in daftar_buku:
    print("-", b["judul"])

buku_baru = [b["judul"] for b in daftar_buku 
            if b["tahun"] >= 2025]
print("Buku terbit 2020 ke atas:", buku_baru)
print("\n===========================================")


print("===========================================")
print("\n--- 6. Comprehension & Utilitas ---")
angka_1_20 = range(1, 21)
genap = [x for x in angka_1_20 if x % 2 == 0]
kuadrat = [x**2 for x in angka_1_20]
print("Genap 1-20:", genap)
print("Kuadrat 1-20:", kuadrat)

dict_ganjil_genap = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("Dict comprehension 1-10:", dict_ganjil_genap)

teks = "Hello World"
huruf_unik = {huruf.lower() for huruf in teks if huruf != " "}
print("Set comprehension huruf unik dari kata Hello World:", huruf_unik)
print("===========================================") 


print("===========================================")
print("\n--- 7. Keanggotaan & Pencarian ---")
cari_angka = 3.14
if cari_angka in list_campur:
    indexnya = list_campur.index(cari_angka)
    print(cari_angka, "ada di dalam list soal pertama pada index", indexnya)
else:
    print(cari_angka, "tidak ada di dalam list")

cari_set = 5
if cari_set in himpunan1:
    print(cari_set, "ditemukan di dalam himpunan1 dari soal nomor 3")
else:
    print(cari_set, "tidak ditemukan")