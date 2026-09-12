nama = "Zakki Zakwan" #string
umur = 20 #int
tinggi = 167.5 #float
is_mahasiswa = True #boolean
hobi = ["Makan", "Masak"] #list

print("============================")
print("Variabel dan Tipe Data")
print("string --- Nama:", nama)
print("integer --- Umur:", umur)
print("float --- Tinggi:", tinggi)
print("boolean --- Mahasiswa:", is_mahasiswa)
print("list --- Hobi:", hobi)
print("============================\n")


kalimatSatu = "Belajar di Infinite Learning"
kalimatDua = "AI Batch"
kataTiga = "11"

gabungan = kalimatSatu + " " + kalimatDua + " " + kataTiga

print("============================")
print("Manipulasi String\n")
print("Teks gabungan:", gabungan)
print("Panjang string:", len(gabungan))
print("Huruf besar:", gabungan.upper())
print("Huruf kecil:", gabungan.lower())
print("===========================\n")


buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Anggur"]
buah.append("Semangka")
buah.remove("Pisang")

print("============================")
print("List dan Akses Elemen")
print("List awal: ", buah)
print("Elemen ke-3: ", buah[2])
print("Setelah ditambah Semangka: ", buah)
print("Setelah Pisang dihapus:  ", buah)
print("============================\n")

print("============================\n")
print("Penggunaan Input Dari User")
inputNama = input("Masukkan nama Anda: ")
inputUmur = input("Masukkan umur Anda: ")
print("Halo, nama saya" + inputNama + " dan umur saya " + inputUmur + " tahun.") 
print("============================\n")