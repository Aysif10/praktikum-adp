print("DAFTAR PAKET MAKANAN: ")
print("kode paket : 1")
print("paket : ayam")
print("harga : Rp20.000")
print("kode paket : 2")
print("paket : sapi")
print("harga : Rp35.000")
print("kode paket : 3")
print("paket : cumi-cumi")
print("harga : Rp45.000")

kode = int(input("silahkan masukkan kode paket makanan(1-3) : "))

if kode==1 :
    print( "paket ayam")
    harga = 20000
    print(f'harga paket :Rp.{harga}')
if kode==2 :
    print( "paket sapi")
    harga = 35000
    print(f'harga paket : Rp.{harga}')
if kode==3 :
    print( "paket cumi-cumi")
    harga = 45000
    print(f'harga paket : Rp.{harga}')

jarak = float(input('masukkan jarak :'))

if jarak < 1:
    ongkir = 0
elif 1<=jarak<=3:
    ongkir = 7000
else :
    ongkir = 15000

total_biaya = harga + ongkir

nama = str(input("Nama Pembeli = "))
print("struk pemesanan")
print(f'nama pembeli : {nama}')
print(f'kode paket : {kode}')
print(f'harga paket : {harga}')
print(f'ongkir : {ongkir}')
print(f'total biaya : {total_biaya}')

