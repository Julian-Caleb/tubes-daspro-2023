# { FUNCTION LOAD }
# { Function Load menerima sebuah string yang menjadi nama folder tempat file csv disimpan dan mengekstrak 11 CSVArray dari file-file tersebut.
# I.S. sebuah string 
# F.S. 11 CSVArray }

# { KAMUS LOKAL }
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >

# CSVUSername, CSVPassword, CSVRole : CSVArray
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVDeskripsi, CSVJumlah : CSVArray

# function os.path.exists (namaFolder : string) -> Boolean
# function exit() 
# { fungsi terdefinisi untuk keluar dari program }
# { fungsi terdefinisi yang mengecek apakah terdapat folder namaFolder dalam folder program berada }
# function os.path.join(namaFolder1 : string, namaFolder2 : string) -> string
# { fungsi terdefinisi yang menyatukan beberapa string menjadi path folder }
# function CSVParser (CSVfile : string, columnName : string) -> CSVArray
# function LengthArray (arr: arr) -> integer

# ALGORITMA
# import
import os
import argparse
from TipeBentukan import CSVArray
from CSVParser import CSVParser
from AdditionalFunction import LengthArray

def Load(namaFolder : str) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray):
    
    # Validasi apakah namaFolder ada atau tidak
    # jika tidak ada
    if not os.path.exists(namaFolder):
        print("Folder \"" + namaFolder + "\" tidak ditemukan.")
        exit()
    
    # jika ada
    else : # os.path.exists(namaFolder)
            
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
        
        # keluarkan pesan 
        print("Loading...")
        print("Data berhasil dimuat!")
        print("Selamat datang di program \"Manajerial Candi\"")       

        return (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah)
    
    
    
    
