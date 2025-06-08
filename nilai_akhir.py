data=[
    "2410431013,aysi,98,100,98",
    "2410431014,dela,90,85,100",
    "2410431015,thya,70,70,91",
    "2410431016,tasya,35,10,85",
    "2410431017,lila,5,20,98",
    "2410431018,sali,45,50,96",
    "2410431019,bima,0,100,100",
    "2410431020,sisi,55,70,95",
    "2410431021,naira,65,100,100",
    "2410431022,sami,50,60,100",
]

with open("data_praktikan.txt","w") as file:
    for line in data:
        file.write(line+ "\n")

data_dictionary={}
with open("data_praktikan.txt","r") as file:
    bariss=file.readlines()
    for baris in bariss:
        NIM,Nama,Pretest,Postest,Tugas = baris.strip().split(",")
        data_dictionary[NIM]= {
            "Nama":Nama,
            "Nilai Pretest":float(Pretest),
            "Nilai Postest":float(Postest),
            "Nilai Tugas":float(Tugas)
            }
with open("data_nilai_akhir.txt","w")as file:
    file.write(f"{'NIM':<12} {'Nama':<6} {'Pretest':<8} {'Postest':<8} {'Tugas':<6} {'Nilai Akhir':<10}\n")
    file.write("-" * 60 + "\n")
    for NIM, data in data_dictionary.items():
         data=data_dictionary[NIM]
         nilai_akhir = 0.35 * data['Nilai Pretest'] + 0.35 * data['Nilai Postest'] + 0.30 * data['Nilai Tugas']
         data["Nilai Akhir"]= float(round(nilai_akhir,2))
         file.write(f"{NIM:<12} {data['Nama']:<6} {data['Nilai Pretest']:<8} {data['Nilai Postest']:<8} {data['Nilai Tugas']:<6} {data['Nilai Akhir']:<10}\n")
total=0
jumlah=0
nim_tertinggi=0
nim_terendah=0
nilai_tertinggi=None
nilai_terendah=None

for NIM in data_dictionary:
    nilai=data_dictionary[NIM]["Nilai Akhir"]
    total+=nilai
    jumlah+=1
    if nilai_tertinggi is None or nilai > nilai_tertinggi:
        nilai_tertinggi=nilai
        nim_tertinggi=NIM
    elif nilai_terendah is None or nilai < nilai_terendah:
        nilai_terendah=nilai
        nim_terendah=NIM

rata_rata=total/jumlah

bawah_rata2=0
for NIM in data_dictionary:
    if data_dictionary[NIM]["Nilai Akhir"] < rata_rata:
        bawah_rata2+=1

print(f"Nilai tertinggi:",data_dictionary[nim_tertinggi]["Nama"],"(",nim_tertinggi,")",nilai_tertinggi)
print(f"Nilai terendah:",data_dictionary[nim_terendah]["Nama"],"(",nim_terendah,")",nilai_terendah)
print(f"rata-rata:{rata_rata}")
print(f"Jumlah dibawah rata-rata:{bawah_rata2}")




