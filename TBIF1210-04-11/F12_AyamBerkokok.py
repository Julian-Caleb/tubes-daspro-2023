from CSVParser import CSVParser
from typing import List
from TipeBentukan import CSVArray
from AdditionalFunction import MemberOf, IndexOf, Delete, LengthArray, AppendCSVArray, DeleteCSVArray, AmbilBahan
from BonusFunction import Lcg_rng

# PROCEDURE AYAMBERKOKOK
# Procedure AyamBerkokok yang hanya dapat diakses oleh Roro Jonggrang (role “roro_jonggrang”) menerima sebuah CSVArray, menghitung jumlah candi yang sudah dibangun berdasarkan CSVArray tersebut, dan menentukan pemenang berdasarkan jumlah candi 
# 	I.S. sebuah CSVArray
# 	F.S. pesan pemenang

# KAMUS LOKAL
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
	
# CSVId : CSVArray

# jumlahCandi : integer

# function exit() fungsi bawaan python untuk keluar dari program

def AyamBerkokok(CSVId : CSVArray):
    # Mengeluarkan pesan awal
    print("Kukuruyuk.. Kukuruyuk..\n")

    # Menghitung banyak candi yang sudah dibangun
    jumlahCandi = CSVId.Neff
    print(f"Jumlah candi: {jumlahCandi}\n")

    # Menentukan pemenang
    if jumlahCandi != 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        
    # Keluar
    exit()