print("______________Khoaerunnisa Isnaeni Lestari_______________")
kontak = [
    {'Nama':'Ari', 'Telp':'081267888'},
    {'Nama':'Dina', 'Telp':'087677776'}
]
   
print("Tampilan Kontak")
print(" Nama | Kontak |")
print("======================")
for key in kontak:
      print(f"{key['Nama']} | {key['Telp']}")
print("Tampilkan kontak Ari:", kontak[1])
print("Tambah kontak Riko")

riko = {'Nama':'Riko','Telp':'087654544'}
kontak.append(riko)
print("Kontak barunya: ", kontak[2])
kontak[1]['Telp'] = '088999776'
print("Setelah no diubah : ", kontak[1])
print("Menampilkan Nama")
for p in kontak:
    print(p['Nama'])
print("Menapilkan daftar kontak")
print("Nama | Kontak |")
print("=========================")
for key in kontak:
      print(f"{key['Nama']} | {key['Telp']}")
print("Hapus kontak Dina")
del kontak[1]
print("Menapilkan daftar kontak")
print("Nama | Kontak |")
print("=========================")
for key in kontak:
    print({key['Nama']} | {key['Telp']})
    