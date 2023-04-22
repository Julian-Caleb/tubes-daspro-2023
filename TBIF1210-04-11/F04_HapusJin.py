from typing import List
from TipeBentukan import CSVArray
from AdditionalFunction import MemberOf, IndexOf, Delete, Frequency

# FUNCTION HAPUSJIN 
# Fungsi HapusJin menerima role, 8 buah CSVArray, yaitu CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, meminta input jin yang ingin dihapus dari user, dan menghapus jin tersebut (serta candi-candi yang dibuat) dari array serta mengembalikannya
#   I.S. role, 8 CSVArray untuk username, password, role, id, pembuat, pasir, batu, dan air
#   F.S. mengembalikan 8 CSVArray namun dengan segala yang berhubungan dengan jin input user sudah dihapus jika input valid 

# KAMUS LOKAL 
# constant Nmax : integer = 103
# usernameJin : string
# konfirmasi : char

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVUsername, CSVPassword, CSVRole : CSVArray
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray

# index : integer

# function IndexOf (arr : List, keyword : string) -> integer
# function MemberOf (arr : List, keyword : string) -> boolean
# function Delete (arr : List, index : integer) -> List

def HapusJin (role : str, CSVUsername : CSVArray, CSVPassword : CSVArray, CSVRole : CSVArray, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray) :
    
    # Mengecek apakah (role) diisi dengan "bandung_bondowoso"
    # Jika tidak
    if role != "bandung_bondowoso":
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    
    # Jika ya, input nama jin ke dalam (usernameJin)
    else:
        
        # jika belum ada jin
        if (Frequency (CSVRole.arr, "jin_pengumpul") + Frequency(CSVRole.arr, "jin_pembangun")) == 0 :
            print("Belum ada jin yang dibuat, silahkan summon jin terlebih dahulu.")
        
        # jika sudah ada
        else :
            usernameJin = str(input("Masukkan username jin : "))

            # Jika (usernameJin) tidak terdaftar pada (CSVUsername)
            if (not(MemberOf(CSVUsername.arr, usernameJin))) :
                print("Tidak ada jin dengan username tersebut.")
                
            # Jika (usernameJin) terdaftar pada (CSVUsername)
            else:
                
                # mengecek apakah username tersebut merupakan jin atau bukan 
                # mencari index 
                index = IndexOf(CSVUsername.arr, usernameJin)
                
                if (CSVRole.arr[index] == "bandung_bondowoso") or (CSVRole.arr[index] == "roro_jonggrang") :

                    # kirim pesan 
                    print("Tidak ada jin dengan username tersebut.")

                else : # (CSVRole.arr[index] == "jin_pembangun") or (CSVRole.arr[index] == "jin_pengumpul") 

                    # meminta konfirmasi 
                    print("Apakah anda yakin ingin menghapus jin dengan username:", usernameJin, "(Y/N)?", end = " ")
                    konfirmasi = input()
                                    
                    # jika ya, 
                    if (konfirmasi == "Y") or (konfirmasi == "y") :

                        # menghapus dari CSVUsername, CSVPassword, CSVRole 
                        # mencari index 
                        index = IndexOf(CSVUsername.arr, usernameJin)
                    
                        # menghapus dari array dengan menjadikan None 
                        CSVUsername.arr = Delete (CSVUsername.arr, index)
                        CSVUsername.Neff = CSVUsername.Neff - 1

                        CSVPassword.arr = Delete (CSVPassword.arr, index)
                        CSVPassword.Neff = CSVPassword.Neff - 1

                        CSVRole.arr = Delete (CSVRole.arr, index)
                        CSVRole.Neff = CSVRole.Neff - 1
                            
                        #  menghapus dari CSVCandi 
                        #  selama masih menjadi member, 
                        while (MemberOf(CSVPembuat.arr, usernameJin)) :
                            #  cari indexnya, 
                            index  = IndexOf(CSVPembuat.arr, usernameJin)
                                
                            #  dan hapus elemennya dengan dijadikan None 
                            CSVId.arr = Delete (CSVId.arr, index)
                            CSVId.Neff = CSVId.Neff - 1

                            CSVPembuat.arr = Delete (CSVPembuat.arr, index)
                            CSVPembuat.Neff = CSVPembuat.Neff - 1

                            CSVPasir.arr = Delete (CSVPasir.arr, index)
                            CSVPasir.Neff = CSVPasir.Neff - 1

                            CSVBatu.arr = Delete (CSVBatu.arr, index)
                            CSVBatu.Neff = CSVBatu.Neff - 1

                            CSVAir.arr = Delete (CSVAir.arr, index)
                            CSVAir.Neff = CSVAir.Neff - 1
                        
                        # keluarkan pesan 
                        print("Jin telah berhasil dihapus dari alam gaib.")

                    # jika tidak, 
                    else : # konfirmasi == “N” 
                        print("Penghapusan jin dibatalkan.") 

                    
    return (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)