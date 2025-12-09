class Mahasiswa:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        
class Pria(Mahasiswa):
    def show(self):
        print(f'Nama saya {self.nama}, dan jenis kelamin saya {self.jenis}')

class Wanita(Mahasiswa):
    def show(self):
        print(f'Nama saya {self.nama}, dan jenis kelamin saya {self.jenis}')

x = Pria('Fairuz', 'Laki-laki')
y = Wanita('Rukkayyah', 'Perempuan')

x.show()
y.show()