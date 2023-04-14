def loginJin(x):
    usernameJin = ["" for i in range(x)]
    passwordJin = ["" for i in range(x)]
    z = 0
    while(z < x):
        usernameJin = str(input("Masukkan username jin: "))
        passwordJin = str(input("Masukkan password jin: "))
        if(usernameJin[z] == ""): # belum lengkap kalau username sama
            print("Username", usernameJin, "sudah diambil!")
        else:
            if(len(passwordJin) < 5 or len(passwordJin) > 25):
                print("Password panjangnya harus 5-25 karakter!")
            else:
                z = z + 1
                print("Mengumpulkan sesajen…")
                print("Menyerahkan sesajen…")
                print("Membacakan ")
                print("Jin", usernameJin, "berhasil dipanggil!")

    for i in range (x): # Buat nyetak list
        print(usernameJin, passwordJin)


def summonJin(y, username):
    Nmax = 103
    if(username != "bandung_bondowoso"):
        print("") # pesan kalau bukan bandung_bondowoso apa?
    else:
        if(y == Nmax):
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            print("Jenis jin yang dapat dipanggil:")
            print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            ("(2) Pembangun - Bertugas membangun candi")
        for i in range(y):
            nomor = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if(nomor == 1):
                print("Memilih jin “Pengumpul”.")
                roleJin = "jin_pengumpul"
                print(loginJin(y))
            elif(nomor == 2):
                print("Memilih jin “Pembangun”.")
                roleJin = "jin_pembangun"
                print(loginJin(y))
            else:
                print("Tidak ada jenis jin bernomor", nomor, "!")




        