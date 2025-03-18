while True :
    angka_pertama = float(input("masukkan angka pertama = "))
    angka_kedua = float(input("masukkan angka kedua = "))

    print("""
    KALKULATOR
pilihan operasi bilangan:
1. penjumlahan
2. pengurangan
3. perkalian
4. pembagian
5. keluar
 """)

    pilihan = int(input("pilih operasi yang kamu inginkan(ketik angka)  = "))
    
    if pilihan==1:
        hasil = angka_pertama+angka_kedua
        print("hasil penjumlahannya = ", hasil)
    elif pilihan==2:
        hasil = angka_pertama-angka_kedua
        print("hasil pengurangannya = ", hasil)
    elif pilihan==3:
        hasil = angka_pertama*angka_kedua
        print("hasil perkaliannya = ", hasil)
    elif pilihan==4:
        if angka_kedua==0 :
            print("error")
        else :
            hasil = angka_pertama/angka_kedua
            print("hasil pembagiannya = ", hasil)
    elif pilihan==5:
        print("selesai menggunakan kalkulator")
        break
    else :
        print("tidak ada pilihan")
    print('\n')


