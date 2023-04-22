from CSVParser import CSVParser
from TipeBentukan import CSVArray
from typing import List
from TipeBentukan import CSVArray
from AdditionalFunction import MemberOf, IndexOf, Delete, Frequency

# FUNCTION UBAHJIN 
# Fungsi UbahJin menerima role dan 7 CSVArray yaitu CSVUsername, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, meminta username input dari user, mendeteksi apakah ada username pada CSVUsername, dan meminta konfirmasi jika tipenya ingin diubah (jika ada). Jika tipe diubah dari pembangun ke pengumpul, candi yang dibuat akan dihancurkan
#   I.S. role dan 7 buah CSVArray sembarang
#   F.S. 7 buah CSVArray namun dengan perubahan berdasarkan input user

# KAMUS LOKAL

# constant Nmax : integer = 103

# role : string
# roleJin, roleJinAwal, roleJinAkhir : string
# konfirmasi : char
# username : string

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVUsername, CSVRole : CSVArray
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray

# function MemberOf (arr : List, keyword : string) -> boolean
# function Delete (arr : List, index : integer) -> List

def UbahJin (role : str, CSVUsername : CSVArray, CSVPassword : CSVArray, CSVRole : CSVArray, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray) :

    # Mengecek apakah (role) diisi dengan "bandung_bondowoso"
    # Jika tidak
    if role != "bandung_bondowoso":
        print ("Ubah jin hanya dapat diakses oleh Bandung Bondowoso.")
    
    # Jika ya
    else:
        
        # jika belum ada jin
        if (Frequency (CSVRole.arr, "jin_pengumpul") + Frequency(CSVRole.arr, "jin_pembangun")) == 0 :
            print("Belum ada jin yang dibuat, silahkan summon jin terlebih dahulu.")

        else :
            
            # Searching apakah ada atau tidak, jika ada
            if (MemberOf(CSVUsername.arr, usernameJin)) :
                index = IndexOf(CSVUsername.arr, usernameJin)
                roleJin = CSVRole.arr[index]

                # berubah ke apa
                if (roleJin == "jin_pembangun"):
                    roleJinAwal = "Pembangun"
                    roleJinAkhir = "Pengumpul"
                    roleJin = "jin_pengumpul"		
                else:
                    roleJinAwal = "Pengumpul"
                    roleJinAkhir = "Pembangun"
                    roleJin = "jin_pembangun"
                # meminta konfirmasi
                print(f"Jin ini bertipe {roleJinAwal}. Yakin ingin mengubah ke tipe {roleJinAkhir} (Y/N)?", end=" ")
                konfirmasi = str(input())

                if (konfirmasi == "Y"):
                    # mengubah role
                    CSVRole.arr[index] = roleJin
                    print("Jin telah berhasil diubah.")
                else:
                    print("Pengubahan jin dibatalkan.")

            # jika tidak ada username
            else:
                print("Tidak ada jin dengan username tersebut.")
            
    return (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)
