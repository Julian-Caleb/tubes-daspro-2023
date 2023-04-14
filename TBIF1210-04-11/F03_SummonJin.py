ddef loginJin(x):
    usernameJin = ["" for i in range(x)]
    passwordJin = ["" for i in range(x)]
    z = 0
    while(z < x):
        usernameJin = str(input("Masukkan username jin: "))
        passwordJin = str(input("Masukkan password jin: "))
        if(usernameJin[z] == ""): # belum lengkap buat condition username jin sama
            print("Username", usernameJin, "sudah diambil!")
        else:
            if(len(passwordJin) < 5 or len(passwordJin) > 25): # ketentuan password
                print("Password panjangnya harus 5-25 karakter!")
            else:
                z = z + 1 # lanjut ke input selanjutnya kalau password udah bener
                print("Mengumpulkan sesajen…")
                print("Menyerahkan sesajen…")
                print("Membacakan ")
                print("Jin", usernameJin, "berhasil dipanggil!")

    for i in range (x): # buat nyetak list (gk termasuk ke spek, cmn buat liat aja kalau username & password bener jadi list)
        print(usernameJin, passwordJin)

def summonJin(y, username):
    Nmax = 103
    if(username != "bandung_bondowoso"):
        print("") # pesan kalau bukan bandung_bondowoso apa?
    else:
        if(y == Nmax): # kalau jin udh maksimal?
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            print("Jenis jin yang dapat dipanggil:")
            print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("(2) Pembangun - Bertugas membangun candi")
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


                
                
# INI BUAT KALAU USERNAME SAMA, CUMAN BELUM JALAN. PAS DI RUN MASIH OUT OF INDEX (line 57)
x = 3 # panjang list contoh
a = [0 for i in range(x)]
j = 0
while(j < x): # loop input
    a = str(input("Masukkan username jin: "))
    for k in range (j-1):
        if(a[j] == a[k]): # nilai input sekarang dibandingkan dengan nilai input sebelumnya, hingga index sebelum index input sekarang (-1)
            print("sama")
    j = j + 1


        
