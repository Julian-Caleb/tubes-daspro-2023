# PROGRAM UTAMA
# 

# KAMUS GLOBAL
# constant NMax = 100

# username : string 
# password : string
# role : string
# func : string 
# isLoggedIn : boolean

# CSVfile : string
# type CSVArray : <arr : array [0..NMax-1] of string,
# 				Neff : integer >
# CSVUsername : CSVArray
# CSVPassword : CSVArray
# CSVRole : CSVArray

# ALGORITMA
# import function
from CSVParser import CSVParser
from AdditionalFunction import Length, LengthArray
from TipeBentukan import CSVArray
from F01_login import Login
from F02_logout import Logout
from F04_HapusJin import HapusJin
from F05_UbahJin import UbahJin
from F06_Bangun import Bangun

# main program
# inisialisasi variable
(username, password, role, isLoggedIn) = ("", "", "", False)

# mengambil array yang dibutuhkan
CSVfile = "user.csv"
CSVUsername = CSVArray(CSVParser(CSVfile, "username"), LengthArray(CSVParser(CSVfile, "username")))
CSVPassword = CSVArray(CSVParser(CSVfile, "password"), LengthArray(CSVParser(CSVfile, "password")))
CSVRole = CSVArray(CSVParser(CSVfile, "role"), LengthArray(CSVParser(CSVfile, "role")))

CSVfile = "candi.csv"
CSVId =  CSVArray(CSVParser(CSVfile, "id"), LengthArray(CSVParser(CSVfile, "id")))
CSVPembuat = CSVArray(CSVParser(CSVfile, "pembuat"), LengthArray(CSVParser(CSVfile, "pembuat")))
CSVPasir = CSVArray(CSVParser(CSVfile, "pasir"), LengthArray(CSVParser(CSVfile, "pasir")))
CSVBatu = CSVArray(CSVParser(CSVfile, "batu"), LengthArray(CSVParser(CSVfile, "batu")))
CSVAir = CSVArray(CSVParser(CSVfile, "air"), LengthArray(CSVParser(CSVfile, "air")))

CSVfile = "bahan_bangunan.csv"
CSVNama = CSVArray(CSVParser(CSVfile, "nama"), LengthArray(CSVParser(CSVfile, "nama")))
CSVDeskripsi = CSVArray(CSVParser(CSVfile, "deskripsi"), LengthArray(CSVParser(CSVfile, "deskripsi")))
CSVJumlah = CSVArray(CSVParser(CSVfile, "jumlah"), LengthArray(CSVParser(CSVfile, "jumlah")))        

# looping 
while True :
    func = input(">>> ")
    
    # F01 - Login
    if func == "login" :
        (username, password, role, isLoggedIn) = Login(username, password, role, isLoggedIn, CSVUsername, CSVPassword, CSVRole)
        # print (username, password, role, isLoggedIn)
        
    # F02 - Logout
    elif func == "logout" :
        (username, password, role, isLoggedIn) = Logout(isLoggedIn)
        # print (username, password, role, isLoggedIn)
        
    # F03 - Summon Jin
    
    # F04 - Hapus Jin
    elif func == "hapusjin" :
        (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = HapusJin(role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)
        # print(CSVId.arr)
        # print(CSVUsername.arr)

    # F05 - Ubah Jin
    elif func == "ubahjin" :
        (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = UbahJin(role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)

    # F06 - Bangun Candi
    elif func == "bangun" :
        (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = Bangun(role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)

