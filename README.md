# Praktikum_5
## Dictionary
Dictionary merupakan tipe data pada Python yang berfungsi untuk menyimpan kumpulan data atau nilai, yang setiap urutanya berisi key dan value. Jika biasanya kita ingin mengakses nilai pada list menggunakan indeks, di dictionary ini kita perlu kata kunci (key) untuk mengakses nilainya.
## Latihan Membuat Dictionary
• Buat Dictionary daftar kontak
Nama sebagai key, dan nomor sebagai value 
Nama | Nomor Telepon
Ari  | 081267888
Dina | 087677776.

• Tampilkan kontaknya Ari menggunakan perulangan for key untuk mengulang nama dan kontak tidak lupa memasukkan index yang ingin diulang. Kemudian tambah kontak baru dengan nama Riko, nomor 08765454, membuat dict baru riko dengan memasukkan ( Nama : Riko | Telp : 08765454), dan ditambahkan kedalam dict kontak dengan statement append, maka riko sudah masuk ke dalam daftar kontak.

• Ubah kontak Dina dengan nomor baru 088999776 dengan memasukkan dari index kontak lalu pilih values "Telp" untuk megubah nomor telepon kemudian tampilkan no setelah diubah lalu tampilkan semua Nama dengan statement perulangan, dan mengektrak list "Nama", maka semua nama akan ditampilkan. 

• Tampilkan semua Nomor, daftar Nama serta nomornya menggunakan perulangan statement for key untuk megulang nama dan kontak, terakhir ialah hapus kontak Dina mengguanakan statement del dict[] kemudian masukkan index berapa yang ingin dihapus.
![iniiii](https://user-images.githubusercontent.com/115929351/204431286-44409efe-448c-4a75-8397-c0711dc7132a.png)

## Output Latihan 5
![iniaja](https://user-images.githubusercontent.com/115929351/204431321-d1980a0d-e108-44a0-b5da-3dd8483b93f1.png)
• Berikut adalah tampilan dari menampilkan daftar kontak Ari dan Dina, dilanjutkan dengan menampilkan kontak Ari (Nama : Ari | Nomor Telepon :  081267888)

• Kemudian mengubah kontak dina dengan no baru, dan menampilkan no barunya Dina. Kemudian menampilkan key dari dictionary yaitu nama nya saja dan terakhur adalah menampilkan dictionary nama dan telp yang dilanjut dengan menghapus kontak Dina dan yang tersisa hanya kontak Ari dan Riko saja.

## Membuat Daftar Nilai
Buat program sederhana yang akan menampilkan daftar nilai
mahasiswa, dengan ketentuan

• Program dibuat dengan menggunakan Dictionary

• Tampilkan menu pilihan: (Tambah Data, Ubah Data, Hapus Data,
Tampilkan Data, Cari Data)

• Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%,
uts: 35%, uas: 35%)

• Buat flowchart dan penjelasan programnya pada README.md. 

• Commit dan push repository ke github.
## Flowchart Program Daftar Nilai
![image](https://user-images.githubusercontent.com/115929351/204506446-b9a82606-08b2-4653-b1e1-04cc51c707c1.png)
PENJELASAN
1. Mulai
2. Ditampilkan menu pilihan (Lihat, Ubah, Cari, Tambah, Hapus dan Keluar) user menginput salah satu pilihan untuk nantinya diproses
3. Ditampilkan kembali input an jika user memilih "tambah" berarti, user memasukkan input an (Nama, NIM, Nilai Tuags, UTS, UAS)
4. Data akan diproses seusai yang user input
5. Menampilkan hasil output "Program Daftar Nilai"
6. Menampilkan keputusan unutk memilih kembali menu pilihan (Lihat, Ubah, Cari, Tambah, Hapus dan Keluar), jika memilih "cari" maka user kembali memasukkan input an baris mana yang mau dicari, dan data akan diproses kembali kemudian menampilkan ulang "Program Daftar Nilai"
7. Menampilkan kembali keputusan menu pilihan (Lihat, Ubah, Cari, Tambah, Hapus dan Keluar), jika user memilih "keluar" maka lalu pilih "y" maka akan secara otomatis keluar dari program tersebut
8. Selesai

## Step by Step
1. Membuat dictionary kosong [], kemudian saya mengguanakan fungsi def untuk memanggil setiap proses menu, setiap kali dipanggil. Membuat index dari kolom ( No, Nama, NIM, Tugas, UTS, UAS, Nilai Akhir) dengan perulangan for dan memberikan nomor dengan enumarate.
2. Membuat input an menu pilihan: (Tambah Data, Ubah Data, Hapus Data, Tampilkan Data, Cari Data) mengguanakan statement if atau pilihan kondisi, 
3. If perintah "t" yaitu tambah data, saya membuat input an memasukkan (Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS) dan membuat rumus untuk nilai akhir nantinya, kemudian saya membuat dict (main) yang berisi key itu semua dan menggabungkan dengan method append dan membuat tampilan kolom (N0, Nama, NIM, Tugas, UTS, UAS, Nilai Akhir) untuk memunculkan data mahasiswa. 
4. Elif perintah "k" yaitu keluar,saya membuat variable inputan untuk menanyakan yakin untuk keluar?, if atau jika iya maka saya memakai fungsi break untuk jeda atau keluar dari program.
5. Elif perintah "h" yaitu hapus, saya membuat input an integer mau menghapus baris ke berapa?, dan memakai methods pop untuk menghapus data berdasarkan index/baris yang diinput.
![cing](https://user-images.githubusercontent.com/115929351/204437799-b9de48c4-b27c-408c-95ba-646d4e561526.png)
6. Elif perintah "l" yaitu lihat, saya membuat input an integer mau lihat baris ke berapa?, dan membuat tampilan kolom (No, Nama, NIM, Tugas, UTS, UAS, Nilai Akhir) untuk memunculkan data mahasiswa. Dan memasukkan list inputan ke dalam data, terakhir membuat index untuk setiap posisi data.
7. Elif perintah "u" yaitu ubah, saya membuat input an variable x,y untuk menanyakan mau ubah baris ke berapa serta kolom berapa, dan input an nilai ganti untuk menanyakan nilai mana yang mau diganti?, kemudian memasukkan variable x,y menjadi list seperti data[x][y] = nilai
8. Elif perintah "c" yaitu cari, saya membuat input an integer mau cari baris berapa?, sama seperti menu "lihat" saya membuat tampilan tampilan kolom (No, Nama, NIM, Tugas, UTS, UAS, Nilai Akhir) untuk memunculkan data mahasiswa. Dan memasukkan list inputan ke dalam data, terakhir membuat index untuk setiap posisi data.
9. Terakhir adalah statement else untuk kondisi lain jika tidak adanya ada yang ditemukan saya menampilkan " Tidak Ada Data Ditemukan"

## Output Daftar Nilai
![cd1](https://user-images.githubusercontent.com/115929351/204443256-361bedbc-3d2e-4330-8412-e640c38f01b4.png)
1. Ini merupakan hasil output dari "Program Daftar Nilai", dan saya memasukkan menu "t" atau tambah maka ini adalah contoh penambahan data, saya memasukkan 2 data dengan menginput (Nama, NIM, Nilai Tugas, UTAS, UAS) dan program akan menampilkan daftar nilai beserta nilai akhir.
![cd 3](https://user-images.githubusercontent.com/115929351/204443715-df635fec-7c88-47f5-8df3-7e27abeaa3b6.png)
2. Dan ini merupakan output dari menu "c" atau cari, saya menginput baris cari no 1 maka program akan menampilkan kolom 1 yaitu data mahasiswi isna
![hapus](https://user-images.githubusercontent.com/115929351/204445162-33068c2b-d83c-4661-98d2-a9b3595f955c.png)
3. Ini merupakan hasil output dari menu "h" atau hapus, saya mempunyai 2 data mahasiswa yaitu Vira dan Noni, kemudian saya mau menghapus data mahasiswi Noni maka saya memasukkan baris 1 sesuai yang tertera pada no, maka yang tersisa hanya data mahasiswi vira.
![oke](https://user-images.githubusercontent.com/115929351/204446988-439e251d-0f53-4d84-8fa1-a70802aac26f.png)
4. Ini adalah hasil output dari menu "l" atau lihat, sama cara kerjanya seperti 'cari' yaitu dengan menginput baris mana yang mau dicari maka data tersebut/yang diminta akan muncul.
![x](https://user-images.githubusercontent.com/115929351/204447343-592dc68d-35ab-473e-8368-887a26f2b19e.png)
5. Ini adalah hasil output menu yang tidak tedapat dari menu pilihan (Tambah Data(t), Ubah Data(u), Hapus Data(h), Tampilkan Data(l), Cari Data(c), Keluar(k)) maka program akan otomatis menampilkan data tersebut tidak ditemukan.
![q](https://user-images.githubusercontent.com/115929351/204445525-e19cd645-acda-47d4-bba3-50c28698f80f.png)
6. Dan ini merupakan hasil output dari menu "k" atau keluar, yaitu jika saya memilih ya untuk keluar maka saya akan keluar dari program, jika tidak maka program akan mengulang menu untuk dipilih.


# Thanks for Read Everyone






