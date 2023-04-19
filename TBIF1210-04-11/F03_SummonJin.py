# import
from TipeBentukan import CSVArray
from typing import List
from AdditionalFunction import Frequency, MemberOf, AppendCSVArray

# { FUNCTION SUMMONJIN }
# { Function SummonJin, yang hanya dapat diakses oleh Bandung Bondowoso, melakukan pembuatan jin apabila jumlah jin dibawah 100, dan mengembalikan pesan apabila jin sudah 100
# 	I.S. array username, password, dan role sembarang, dan role bandung_bondowoso untuk memastikan apakah mendapat akses atau tidak
# 	F.S array username, password, dan role yang sudah ditambah dengan jin yang baru dibuat apabila semua ketentuan terpenuhi }

# { KAMUS LOKAL }
# constant Nmax : integer = 103

# role : string

# nomor : integer [1..2]
# usernameJin, passwordJin, roleJin : string

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVUsername : CSVArray
# CSVPassword : CSVArray
# CSVRole : CSVArray

# function Frequency (arr : List, keyword : string) -> integer
# function MemberOf (arr : List, keyword : string) -> boolean
# function LengthString (str : string) -> integer
# function AppendCSVArray (CSVArray : CSVArray, element : string) -> CSVArray

# ALGORITMA
def SummonJin (role : str, CSVUsername: CSVArray, CSVPassword: CSVArray, CSVRole: CSVArray) -> (CSVArray, CSVArray, CSVArray) :

    if(role != "bandung_bondowoso"):
        return (CSVUsername, CSVPassword ,CSVRole)
    
    else: # role == "bandung_bondowoso"
        if (Frequency (CSVRole.arr, "jin_pengumpul") + Frequency(CSVRole.arr, "jin_pembangun")) == 100 :
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            return (CSVUsername, CSVPassword ,CSVRole)
        
        else: # role : "bandung_bondowoso"
            print("Jenis jin yang dapat dipanggil:")
            print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("(2) Pembangun - Bertugas membangun candi\n")
            
        while True :
            nomor = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if (nomor != 1) and (nomor != 2) :
                print("Tidak ada jenis jin bernomor", nomor, "!")
            else :
                break
        
        if (nomor == 1):
            print("\nMemilih jin “Pengumpul”.\n")
            roleJin = "jin_pengumpul"
        elif (nomor == 2):
            print("\nMemilih jin “Pembangun”.\n")
            roleJin = "jin_pembangun"
        
        while True :
            usernameJin = input("Masukkan username jin: ")
            if MemberOf(CSVUsername.arr, usernameJin) :
                print("Username", usernameJin, "sudah diambil!")
            else : 
                break
        
        while True :
            passwordJin = input("Masukkan password jin: ")
            if len(passwordJin) < 5 or len(passwordJin) > 25 :
                print("Password panjangnya harus 5-25 karakter!")
            else : 
                break

        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print("Jin", usernameJin, "berhasil dipanggil!")

        # print(CSVUsername.arr)
        # Memasukkan data ke dalam array 
        AppendCSVArray(CSVUsername, usernameJin)
        AppendCSVArray(CSVPassword, passwordJin)
        AppendCSVArray(CSVRole, roleJin)

        return (CSVUsername, CSVPassword, CSVRole)
        
