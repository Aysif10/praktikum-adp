titik=[]
for i in range(3):
    x=int(input(f"x{i+1}: "))
    y=int(input(f"y{i+1}: "))
    titik.append([x,y])
print(titik)

sisi_a=((titik[0][0]-titik[0][1])**2 + (titik[0][1]-titik[1][1])**2)**0.5
sisi_b=((titik[1][0]-titik[2][0])**2 + (titik[1][1]-titik[2][1])**2)**0.5
sisi_c=((titik[0][0]-titik[2][0])**2 + (titik[0][1]-titik[2][1])**2)**0.5
print(f"sisi_a = {round(sisi_a,2)}")
print(f"sisi_b = {round(sisi_b,2)}")
print(f"sisi_c = {round(sisi_c,2)}")

if sisi_a==sisi_b or sisi_a==sisi_c or sisi_b==sisi_c:
    print("ketiga titik tersebut membentuk segitiga sama kaki")
else:
    print("ketiga titik tersebut tidak membentuk segitiga sama kaki")
