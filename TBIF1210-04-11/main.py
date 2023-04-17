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
from AdditionalFunction import LengthArray
from TipeBentukan import CSVArray
from F01_Login import Login
from F02_Logout import Logout
from F03_SummonJin import SummonJin
from F04_HapusJin import HapusJin
from F05_UbahJin import UbahJin
from F06_Bangun import Bangun
from F07_Kumpul import Kumpul
from F08_Batch import BatchKumpul
from F11_HancurkanCandi import HancurkanCandi
from F15_Help import Help

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
    elif func == "summonjin" :
        (CSVUsername, CSVPassword, CSVRole) = SummonJin(role, CSVUsername, CSVPassword, CSVRole) 
        # print(CSVUsername.arr)
    
    # F04 - Hapus Jin
    elif func == "hapusjin" :
        (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = HapusJin(role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)
        # print(CSVUsername.arr)

    # F05 - Ubah Jin
    elif func == "ubahjin" :
        (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = UbahJin(role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)
        # print(CSVRole.arr)

    # F06 - Bangun Candi
    elif func == "bangun" :
        (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, sCSVJumlah) = Bangun(username, role, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVJumlah)
        # print (CSVPembuat.arr) 
    
    # F07 - Kumpul Candi
    elif func == "kumpul" :
        CSVJumlah = Kumpul (role, CSVNama, CSVJumlah)
        # print (CSVJumlah.arr) 
    
    # F08 - Batch 
    # Batch kumpul
    elif func == "batchkumpul" :
        CSVJumlah = BatchKumpul (role, CSVRole, CSVNama, CSVJumlah)
        print(CSVJumlah.arr)
    
    # F11 - Hancurkan Candi
    elif func == "hancurkancandi" :
        (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = HancurkanCandi(role, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVJumlah)
        # print(CSVUsername.arr)
        # print(CSVId.arr)
    
    # F15 - Help
    elif func == "help" :
        Help (role)

