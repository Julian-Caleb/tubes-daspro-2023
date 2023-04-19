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
import argparse
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
from F08_Batch import BatchBangun, BatchKumpul
from F10_LaporanCandi import LaporanCandi
from F11_HancurkanCandi import HancurkanCandi
from F12_AyamBerkokok import AyamBerkokok
from F13_Load import Load
from F14_Save import Save
from F15_Help import Help
from F16_Exit import Exit

# main program
# F13 - Load
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folderName', type=str, nargs='?')
    args = parser.parse_args()

    if not args.folderName:
        print("Tidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()
    else:
        (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah) = Load(args.folderName)

# inisialisasi variable
(username, password, role, isLoggedIn) = ("", "", "", False)

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
    elif func == "batchbangun" :
        (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVJumlah) = BatchBangun (role, CSVUsername, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir,  CSVNama, CSVJumlah)
        # print(CSVJumlah.arr)
        # print(CSVId.arr)
        
    # Batch kumpul
    elif func == "batchkumpul" :
        CSVJumlah = BatchKumpul (role, CSVRole, CSVNama, CSVJumlah)
        # print(CSVJumlah.arr)
        
    # F10 - Laporan Candi
    elif func == "laporancandi" :
        LaporanCandi(CSVId, CSVPasir, CSVBatu, CSVAir)
        
    # F11 - Hancurkan Candi
    elif func == "hancurkancandi" :
        (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir) = HancurkanCandi(role, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVJumlah)
        # print(CSVUsername.arr)
        # print(CSVId.arr)
    
    # F12 - Ayam Berkokok
    elif func == "ayamberkokok" :
        AyamBerkokok(CSVId)

    # F14 - Save
    elif func == "save" :
        Save (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah) 
    
    # F15 - Help
    elif func == "help" :
        Help (role)

    # F16 - Exit
    elif func == "exit" :
        Exit (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah)
CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah