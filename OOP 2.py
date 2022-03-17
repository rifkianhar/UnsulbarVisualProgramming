class Buah:
 def __init__(self, inputNama, inputWarna, inputJumlah):
     self.nama = inputNama
     self.warna = inputWarna
     self.jumlah = inputJumlah

Buah1 = Buah('Mangga','Kuning','3 buah')
Buah2 = Buah("Apel","Merah","5 buah")

print(Buah1.nama, Buah1.warna, Buah1.jumlah)
