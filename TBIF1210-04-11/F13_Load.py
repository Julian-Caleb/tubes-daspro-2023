# FUNCTION LOAD
# Function Load 
#   I.S.
#   F.S.

# KAMUS LOKAL
#

# ALGORITMA
# import
import os
import argparse
from TipeBentukan import CSVArray
from CSVParser import CSVParser
from AdditionalFunction import LengthArray

def Load(namaFolder : str) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray):
    
    # Validasi apakah folder_name ada atau tidak
    # jika tidak ada
    if not os.path.exists(namaFolder):
        print("Folder \"" + namaFolder + "\" tidak ditemukan.")
        exit()
    
    # jika ada
    else : # os.path.exists(folder_name)
    
        # keluarkan pesan 
        print("Loading...")
        print("Data berhasil dimuat!")
        print("Selamat datang di program \"Manajerial Candi\"")
        
        # mengambil array yang dibutuhkan
        CSVfile = os.path.join(namaFolder, "user.csv")
        CSVUsername = CSVArray(CSVParser(CSVfile, "username"), LengthArray(CSVParser(CSVfile, "username")))
        CSVPassword = CSVArray(CSVParser(CSVfile, "password"), LengthArray(CSVParser(CSVfile, "password")))
        CSVRole = CSVArray(CSVParser(CSVfile, "role"), LengthArray(CSVParser(CSVfile, "role")))

        CSVfile = os.path.join(namaFolder, "candi.csv")
        CSVId =  CSVArray(CSVParser(CSVfile, "id"), LengthArray(CSVParser(CSVfile, "id")))
        CSVPembuat = CSVArray(CSVParser(CSVfile, "pembuat"), LengthArray(CSVParser(CSVfile, "pembuat")))
        CSVPasir = CSVArray(CSVParser(CSVfile, "pasir"), LengthArray(CSVParser(CSVfile, "pasir")))
        CSVBatu = CSVArray(CSVParser(CSVfile, "batu"), LengthArray(CSVParser(CSVfile, "batu")))
        CSVAir = CSVArray(CSVParser(CSVfile, "air"), LengthArray(CSVParser(CSVfile, "air")))

        CSVfile = os.path.join(namaFolder, "bahan_bangunan.csv")
        CSVNama = CSVArray(CSVParser(CSVfile, "nama"), LengthArray(CSVParser(CSVfile, "nama")))
        CSVDeskripsi = CSVArray(CSVParser(CSVfile, "deskripsi"), LengthArray(CSVParser(CSVfile, "deskripsi")))
        CSVJumlah = CSVArray(CSVParser(CSVfile, "jumlah"), LengthArray(CSVParser(CSVfile, "jumlah")))        

        return (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah)
    
    
    
    
