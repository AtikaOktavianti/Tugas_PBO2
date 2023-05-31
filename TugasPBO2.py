""" Tugas PBO (Pemrograman Berorientasi Objek)
Nama: Atika Oktavianti
NPM: G1A022020 
Prodi: Informatika (B)"""

class Mahasiswa:
    def __init__(self, nama, nim, jurusan): #Atribut Nama,NIM, dan Jurusan
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_info(self):# Menampilkan informasi Nama,NIM, dan nama Jurusan Mahasiswa
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan): # memiliki atribut NamaJurusan dan DaftarMahasiswa
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    def tambah_mahasiswa(self, mahasiswa): # Menambah objek Mahasiswa ke dalam  DaftarMahasiswa
        self.DaftarMahasiswa.append(mahasiswa)
    
    def tampilkan_daftar_mahasiswa(self):# Menampilkan daftar mahassiswa yang terdaftar dalam Jurusan.
        print("Daftar Mahasiswa", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            mahasiswa.tampilkan_info()


class Universitas:
    def __init__(self, nama_universitas):# memiliki atribut NamaUniversitas dan DaftarJurrusan
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    def tambah_jurusan(self, jurusan): # Menambah objek Jurusan ke dalam  DaftarJurusan
        self.DaftarJurusan.append(jurusan)
    
    def tampilkan_daftar_jurusan(self): # menampilkan daftar jurusan yang ada di Unniversitas
        print("Daftar Jurusan di", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)


# Membuat objek Universitas
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan
jurusan_ti = Jurusan("Teknik Informatika")

# Menambahkan objek Jurusan ke dalam Universitas XYZ
universitas_xyz.tambah_jurusan(jurusan_ti)

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("Atika Oktavianti", "G1A022020", jurusan_ti)

# Menambahkan objek Mahasiswa ke dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tambah_mahasiswa(mahasiswa1)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
