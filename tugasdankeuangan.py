from termcolor import colored
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi animasi loading
def loading(teks="Memproses", lama=3):
    print(f"{teks}", end="")
    for _ in range(lama):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" ✅")

# Fungsi untuk memuat data dari file .txt
def muat_data():
    tugas = []
    keuangan = {"cash": 0, "m-banking": 0, "e-wallet": 0}
    riwayat_pengeluaran = []

    try:
        with open("tugas.txt", "r") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 4:
                    tugas.append(data)
    except: pass

    try:
        with open("keuangan.txt", "r") as f:
            for line in f:
                k, v = line.strip().split("|")
                keuangan[k] = int(v)
    except: pass

    try:
        with open("pengeluaran.txt", "r") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 4:
                    riwayat_pengeluaran.append(data)

    except:pass

    return tugas, keuangan, riwayat_pengeluaran

# Fungsi untuk menyimpan data
def simpan_data(tugas, keuangan, riwayat_pengeluaran):
    with open("tugas.txt", "w") as f:
        for t in tugas:
            f.write("|".join(t) + "\n")
    with open("keuangan.txt", "w") as f:
        for k, v in keuangan.items():
            f.write(f"{k}|{v}\n")
    with open("pengeluaran.txt", "w") as f:
        for r in riwayat_pengeluaran:
            f.write("|".join(r) + "\n")

def warna_prioritas(prio):
    if prio == "Tinggi":
        return colored("Tinggi", "red", attrs=["bold"])
    elif prio == "Sedang":
        return colored("Sedang", "yellow", attrs=["bold"])
    else:
        return colored("Rendah", "green", attrs=["bold"])

def hitung_prioritas():
    hari = int(input("Masukkan jumlah hari sampai deadline: "))
    if hari <= 3:
        return "Tinggi"
    elif 3<hari<= 5:
        return "Sedang"
    else:
        return "Rendah"

def lihat_tugas(tugas):
    if not tugas:
        print(colored("📭 Tidak ada tugas.", "yellow"))
        return

    kolom = [4, 25, 15, 12, 10]
    garis = "+" + "+".join(["-" * k for k in kolom]) + "+"
    print(colored("\n📋 Daftar Tugas:", attrs=["bold"]))
    print(garis)
    print(f"| {'No':<3}| {'Nama':<24}| {'Deadline':<14}| {'Prioritas':<11}| {'Status':<9}|")
    print(garis)

    for i, t in enumerate(tugas):
        no = f"{i+1:<3}"
        nama = f"{t[0]:<24}"
        deadline = f"{t[1]:<14}"
        prio = t[2]
        warna = warna_prioritas(prio)
        pad = " " * (11 - len(prio))
        prioritas = warna + pad
        status_icon = "✅" if t[3] == "Selesai" else "❌"
        status = f"{status_icon} {t[3]}"
        print(f"| {no}| {nama}| {deadline}| {prioritas}| {status:<8}|")

    print(garis)

def tambah_tugas(tugas):
    nama = input("Nama tugas: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    prioritas = hitung_prioritas()
    tugas.append([nama, deadline, prioritas, "Belum"])
    loading("Menyimpan tugas")

def tandai_selesai(tugas):
    lihat_tugas(tugas)
    i = int(input("Pilih nomor tugas yang telah selesai: ")) - 1
    if 0 <= i < len(tugas):
        tugas[i][3] = "Selesai"
        loading("Menandai tugas")
    else:
        print("Nomor tidak valid.")

def hapus_tugas(tugas):
    lihat_tugas(tugas)
    i = int(input("Pilih nomor tugas yang ingin dihapus: ")) - 1
    if 0 <= i < len(tugas):
        tugas.pop(i)
        loading("Menghapus tugas")
    else:
        print("Nomor tidak valid.")

def tambah_pengeluaran(keuangan, riwayat_pengeluaran):
    jenis = input("Pilih dompet (cash/m-banking/e-wallet): ")
    if jenis not in keuangan:
        print("Jenis dompet tidak valid.")
        return
    jumlah = int(input("Jumlah pengeluaran: "))
    kategori = input("Kategori pengeluaran: ")
    tanggal = input("Tanggal pengeluaran (YYYY-MM-DD): ") 
    keuangan[jenis] -= jumlah
    riwayat_pengeluaran.append([tanggal, str(jumlah), kategori, jenis])
    loading("Menyimpan pengeluaran")

def tambah_pemasukan(keuangan):
    jenis = input("Pilih dompet (cash/m-banking/e-wallet): ")
    if jenis not in keuangan:
        print("Jenis dompet tidak valid.")
        return
    jumlah = int(input("Jumlah pemasukan: "))
    keuangan[jenis] += jumlah
    loading("Menyimpan pemasukan")

def lihat_dompet(keuangan):
    print("\nSaldo Dompet:")
    for k, v in keuangan.items():
        warna = "green" if v >= 0 else "red"
        print(f"- {k}: {colored(str(v), warna)}")

def lihat_pengeluaran(riwayat_pengeluaran):
    if not riwayat_pengeluaran:
        print("Belum ada pengeluaran.")
        return
    print(f"\n{'Tanggal':<12} {'Jumlah':<10} {'Kategori':<15} {'Dompet':<10}")
    for r in riwayat_pengeluaran:
        print(f"{r[0]:<12} {r[1]:<10} {r[2]:<15} {r[3]:<10}")

def menu_tugas(tugas):
    while True:
        print(
 """    ==============================
         MENU PENGELOLA TUGAS 
    ==============================
    1. Tambah Tugas
    2. Lihat Tugas
    3. Tandai Selesai
    4. Hapus Tugas
    5. Kembali""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_tugas(tugas)
        elif pilihan == "2":
            lihat_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            hapus_tugas(tugas)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

def menu_keuangan(keuangan, riwayat_pengeluaran):
    while True:
        print(
 """    ===============================
        MENU PENGELOLA KEUANGAN
    ===============================
    1. Tambah Pengeluaran
    2. Tambah Pemasukan
    3. Lihat Dompet
    4. Lihat Riwayat Pengeluaran
    5. Kembali""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_pengeluaran(keuangan, riwayat_pengeluaran)
        elif pilihan == "2":
            tambah_pemasukan(keuangan)
        elif pilihan == "3":
            lihat_dompet(keuangan)
        elif pilihan == "4":
            lihat_pengeluaran(riwayat_pengeluaran)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

# ==== PROGRAM UTAMA ====
tugas, keuangan, riwayat_pengeluaran = muat_data()

print(colored("📱 APLIKASI PENGELOLA TUGAS & KEUANGAN", "cyan", attrs=["bold"]))

while True:
    print(
 """    ==============================
              MENU UTAMA 
    ==============================
    1. Pengelola Tugas
    2. Pengelola Keuangan
    3. Keluar""")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        menu_tugas(tugas)
    elif pilihan == "2":
        menu_keuangan(keuangan, riwayat_pengeluaran)
    elif pilihan == "3":
        loading("Menyimpan data")
        simpan_data(tugas, keuangan, riwayat_pengeluaran)
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid.")