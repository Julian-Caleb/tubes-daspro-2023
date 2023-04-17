# { PROCEDURE HELP }
# { Procedure Help menerima parameter role dan mengeluarkan fungsi fungsi apa saja yang boleh digunakan oleh user berdasarkan role tersebut.
#   I.S. role (antara “ “, “bandung_bondowoso“, “roro_jonggrang”, “jin_pembangun”, atau “jin_pengumpul”)
#   F.S. string menjelaskan fungsi-fungsi yang dapat digunakan }

# { KAMUS LOKAL }
# constant Nmax : integer = 16
# funcArray : array [0..Nmax-1] of real
# funcNoRole, funcBandung, funcRoro, funcPembangun, funcPengumpul: funcArray
# funcHelp : funcArray

# role : string
# i : integer

# { ALGORITMA }
def Help (role : str):
	
    # { inisialisasi funcArray }
    funcNoRole = [1,15,16,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999]
    funcBandung = [2,3,4,5,8.1,8.2,9,10,14,15,9999,9999,9999,9999,9999,9999]
    funcRoro = [2,11,12,14,15,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999]
    funcPembangun = [2,6,14,15,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999]
    funcPengumpul = [2,7,14,15,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999,9999]

    # { cek role }
    if(role == "bandung_bondowoso"):
        funcHelp = funcBandung
    elif(role == "roro_jonggrang"):
        funcHelp = funcRoro
    elif(role == "jin_pembangun"):
        funcHelp = funcPembangun
    elif(role == "jin_pengumpul"):
        funcHelp = funcPengumpul
    else: # { role = “” }
        funcHelp = funcNoRole

    # { iterasi untuk menampilkan help }
    i = 0
    
    # tampilkan pesan awal
    print("=========== HELP ===========")

    while(funcHelp[i] != 9999):
        # { menampilkan help berdasarkan funcarray }
        if(funcHelp[i] == 1): 
            print(f"{i+1}. login")
            print("   Untuk masuk menggunakan akun")
        elif(funcHelp[i]== 2): 
            print(f"{i+1}. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
        elif(funcHelp[i] == 3): 
            print(f"{i+1}. summonjin")
            print("   Untuk memanggil jin baru baik jin pembangun maupun jin pengumpul")
        elif(funcHelp[i] == 4):
            print(f"{i+1}. hapusjin")
            print("   Untuk menghapus jin yang terdaftar")
        elif(funcHelp[i] == 5): 
            print(f"{i+1}. ubahjin")
            print("   Untuk mengubah tipe jin (jin pembangun atau jin pengumpul)")
        elif(funcHelp[i] == 6):
            print(f"{i+1}. bangun")
            print("   Untuk membangun candi")
        elif(funcHelp[i] == 7):
            print(f"{i+1}. kumpul")
            print("   Untuk mengumpulkan bahan-bahan")
        elif(funcHelp[i] == 8.1):
            print(f"{i+1}. batchkumpul")
            print("   Untuk membuat seluruh jin pengumpul mengumpulkan bahan-bahan")
        elif(funcHelp[i] == 8.2):
            print(f"{i+1}. batchbangun")
            print("   Untuk membuat seluruh jin pembangun membangun candi")
        elif(funcHelp[i] == 9):
            print(f"{i+1}. laporanjin")
            print("   Untuk mendapatkan informasi terkait jin yang terdaftar")
        elif(funcHelp[i] == 10):
            print(f"{i+1}. laporancandi")
            print("   Untuk mendapatkan informasi terkait candi yang telah dibangun")
        elif(funcHelp[i] == 11):
            print(f"{i+1}. hancurkancandi")
            print("   Untuk menghancurkan candi yang ada")
        elif(funcHelp[i] == 12):
            print(f"{i+1}. ayamberkokok")
            print("   Untuk menyelesaikan permainan dan menentukan pemenang")
        elif(funcHelp[i] == 13): # { tidak akan digunakan }
            print(f"{i+1}. load")
            print("   Untuk mengambil data tersimpan")
        elif(funcHelp[i] == 14):
            print(f"{i+1}. save")
            print("   Untuk menyimpan data")
        elif(funcHelp[i] == 15):
            print(f"{i+1}. help")
            print("   Untuk menampilkan fungsi-fungsi apa saja yang dapat digunakan")
        else: # { funcHelp[i] = 16 }
            print(f"{i+1}. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
           
        i += 1

# funcHelp[i] = 9999 
