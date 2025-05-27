def menu():
      print("""       Menu
      1. Tabel perkalian modulo n
      2. Mencari nilai Σ x
      3. Mencari nilai n!
      4. Total dan rata rata suatu data
      5. Keluar""" )
def tabel_modulo():
      while True:
             n=int(input("masukkan nilai n(0<n<=10)= "))
             if 0 < n <= 10 :
                   break
      print(f"Tabel perkalian modulo {n}")
      print("   ",end= "")
      for i in range(n):
            print(f"{i:3}",end= "")
      print("\n"+"-"*(n * 3 + 3))
      for i in range(n):
            print(f"{i:2}|",end= "")
            for j in range(n):
                  print(f"{(i * j) % n:3}",end= "")
            print()    
def sigma_x():
      while True:
            batas_bawah=int(input("batas bawah(batas_bawah<=batas_atas) = "))
            batas_atas=int(input("batas atas(batas_atas>=batas_bawah) = "))
            if batas_bawah<= batas_atas:
                  break
      total=0
      for i in range(batas_bawah,batas_atas+1):
            total+=i
      print(f"Σ x = {total}")
def faktorial():
      while True:
            n=int(input("n = "))
            if n>=0:
                  break
      hasil=1
      for i in range(2,n+1):
            hasil*=i
      print(f"{n}! = {hasil} ")
def total_rata2():
      while True:
            n=int(input("Masukkan banyak data(n)="))
            if n>0:
                  break
      data=[]
      total=0
      for i in range(n):
            nilai=float(input(f"masukkan data ke-{i+1}= "))
            data.append(nilai)
            total+=nilai
      rata2= total/n
      print("| {:5}|".format("Data"))
      print("|------|")
      for i in range (len(data)):
            print("|{:5} |".format(data[i]))
      print(f"Total = {total}")
      print(f"Rata-rata = {rata2}")    
while True:
      menu()
      pilihan=int(input("pilih menu(1-5)= "))
      if pilihan == 1:
            tabel_modulo()
      elif pilihan ==2:
            sigma_x()
      elif pilihan ==3:
            faktorial()
      elif pilihan ==4:
            total_rata2()
      elif pilihan ==5:
            print("keluar dari program")
            break
      
            


      