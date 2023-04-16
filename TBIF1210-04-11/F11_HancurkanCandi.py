from CSVParser import CSVParser
from typing import List
from TipeBentukan import CSVArray
from AdditionalFunction import MemberOf, IndexOf, Delete, LengthArray, AppendCSVArray, AmbilBahan
from BonusFunction import Lcg_rng

# FUNCTION HANCURKANCANDI
# Function HancurkanCandi hanya dapat diakses oleh role roro_jonggrang, dimana akan meminta input ID candi yang ingin dihancurkan, dan menghancurkan candi dengan ID tersebut bila ditemukan.
# 	I.S. 1 string dan 7 CSVArray
# 	F.S. 7 CSVArray

# KAMUS LOKAL
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
	
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVJumlah : CSVArray

# idHancur : string
# indexHancur : integer

# function MemberOf (arr : array [0..Nmax-1] of string, keyword : string) -> boolean
# function IndexOf (arr : array [0..Nmax-1] of string, keyword: string) -> integer

def HancurkanCandi(role : str, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray, CSVNama : CSVArray, CSVJumlah : CSVArray) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray):
    
    # Mengecek apakah (role) diisi dengan "roro_jonggrang"
    # Jika tidak
    if role != "roro_jonggrang":
        return (CSVPembuat, CSVPasir, CSVBatu, CSVAir)
    
    else:
        # Input id candi
        idHancur = int(input("Masukkan ID candi: "))

        # Cek jika ada candi
        if MemberOf(CSVId.arr, idHancur):
            # Mencari index
            indexHancur = IndexOf(CSVId.arr, idHancur)

            # Menghancurkan candi
            Delete(CSVId, indexHancur)
            Delete(CSVPembuat, indexHancur)
            Delete(CSVPasir, indexHancur)
            Delete(CSVBatu, indexHancur)
            Delete(CSVAir, indexHancur)

            print("Candi telah berhasil dihancurkan.")
        
        # Jika tidak ada
        else:
            print("Tidak ada candi dengan ID tersebut.")
        
        return (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)