print("_______________ Khaerunnisa Isnaeni Lestari______________")
print("PROGRAM DAFTAR NILAI")
print("========================")

data = []

def manggil():
	for i,x in enumerate(data):
		print("===================================================================")
		print(f"  {i}  |  {x['nama']}  |  {x['nim']}  |   {x['tugas']}   |   {x['uts']}   |   {x['uas']}   |   {x['nilai_akhir']}   |")
		

running = True
while running :
	perintah = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
	if perintah  == "t":
		nama = input("Masukkan Nama :")
		nim = int(input("Masukkan NIM :"))
		tugas = int(input("Masukkan Nilai Tugas : "))
		uts = int(input("Masukkan Nilai UTS : "))
		uas = int(input("Masukkan Nilai UAS : "))
		nilai_akhir =  float(tugas)*30/100+(uts)*35/100+(uas)*35/100
		main = {"nama":nama,"nim":nim, "tugas":tugas, "uts":uts, "uas":uas, "nilai_akhir":nilai_akhir}
		data.append(main)
		print("Menampilkan data")
		print("==================================================================")
		print("  No  |  Nama  |  NIM  |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
		print("==================================================================")
		manggil()
	
	elif perintah == "k":
		a = input("Sure want to quit y/t = ")
		if a == "y":
			break

	elif perintah == "h":
		x = int(input("Baris berapa yang mau dihapus?"))
		data.pop(x)
		manggil()

	elif perintah == "l":
		a = int(input("Masukkan baris ke berapa = "))
		print("==================================================================")
		print("  No  |  Nama  |  NIM  |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
		print("==================================================================")
		n = data[a]
		print(f"  {a}  |  {n['nama']}  |  {n['nim']}  |   {n['tugas']}   |   {n['uts']}   |   {n['uas']}   |   {n['nilai_akhir']}   |")
		

	elif perintah == "u":
		baris = int(input("Masukkan baris yg mau di ganti = "))
		kolom = input("kolom mana yg mau di gant = ")
		nilai = input("niai yang mau di ganti  = ")
		data[baris][kolom] = nilai
		manggil()

	elif perintah == "c":
		c = int(input("Masukkan Baris ke berapa : "))
		print("==================================================================")
		print("  No  |  Nama  |  NIM  |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
		print("==================================================================")
		n = data[c]
		print(f"  {c}  |  {n['nama']}  |  {n['nim']}  |   {n['tugas']}   |   {n['uts']}   |   {n['uas']}   |   {n['nilai_akhir']}   |")
		
	else:
		print("Tidak ada data ditemukan")




		





