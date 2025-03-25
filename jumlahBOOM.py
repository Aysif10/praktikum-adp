print("     -Menghitung Jumlah BOOM-     ")
print()
n = int(input("masukkan nilai n(n>=4) = "))
total_BOOM = 0
print()
for i in range(n):
    for j in range(n):
        if i == j:
            if n % 2 == 1 and i == n // 2:
                print("HORE",end="   ")
            else:
                print(" 1  ",end="   ")
        elif i + j == n - 1:
            print(" 2 ",end="    ")
        else:
            print("BOOM ",end="  ")
            total_BOOM += 1
    print()
print()
if n >= 4:
    print("Total BOOM yang muncul sebanyak =",total_BOOM)
else:
    print("nilai n minimal 4")
print()