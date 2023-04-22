from CSVParser import CSVParser
from typing import List
from TipeBentukan import CSVArray
from AdditionalFunction import MemberOf, IndexOf, Delete, LengthArray, AppendCSVArray, AmbilBahan
from BonusFunction import Lcg_rng

# FUNCTION BANGUN
# Function bangun, yang hanya dapat dilakukan oleh user dengan role jin_pembangun, bertugas untuk membangun candi berdasarkan bahan bangunan yang di randomize (jika bahan cukup, candi dibangun, jika tidak, batal dibangun). Maksimal candi yang dapat dibangun adalah 100 candi, jika lebih maka tidak disimpan. 
#   I.S. 2 string dan 7 CSVArray
#   F.S. 7 CSVArray yang mungkin sudah dimodifikasi berdasarkan candi yang dibangun dan bahan bangunan yang digunakan

# KAMUS LOKAL

# constant Nmax : integer = 103

# username, password, role : string
# pasir, batu, air : integer 
# banyakPasir, banyakBatu, banyakAir : integer
# i : integer

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVDeskripsi, CSVJumlah : CSVArray

# function IndexOf (arr : List, keyword : string) -> integer
# function MemberOf (arr : List, keyword : string) -> boolean
# function AppendCSVArray (CSVArray : CSVArray, element : string) -> CSVArray
# function AmbilBahan (CSVNama : CSVArray, CSVJumlah : CSVArray, argumen : string) -> (integer, integer, integer)

def Bangun (username : str, role : str, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray, CSVNama : CSVArray, CSVJumlah : CSVArray) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray) :

    # Mengecek apakah (role) diisi dengan "jin_pembangun"
    # Jika tidak
    if role != "jin_pembangun":
        
        print ("Bangun hanya dapat diakses oleh jin pembangun.")
    
    else:
        # Bahan yang dibutuhkan untuk membuat candi
        (pasir, batu, air) = AmbilBahan (CSVNama, CSVJumlah, "random")
        # pastikan tidak ada yang 0
        while pasir == 0 or batu == 0 or air == 0 :
            (pasir, batu, air) = AmbilBahan (CSVNama, CSVJumlah, "random")        

        # Cek bahan yang dimiliki
        (banyakPasir, banyakBatu, banyakAir) = AmbilBahan (CSVNama, CSVJumlah, "data")

        # Jika bahan tidak mencukupi
        if pasir > banyakPasir or batu > banyakBatu or air > banyakAir:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else:
            # Mengurangi bahan yang dimiliki
            banyakPasir = banyakPasir - pasir
            banyakBatu = banyakBatu - batu
            banyakAir = banyakAir - air

            # Masukkan kembali ke array
            CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")] = str(banyakPasir)
            CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")] = str(banyakBatu)
            CSVJumlah.arr[IndexOf(CSVNama.arr, "air")] = str(banyakAir)

            # Mencari id yang available antara 1 sampai 100
            i = 1
            while MemberOf(CSVId.arr, str(i)):
                i = i + 1
            
            if i < 101:
                # id
                AppendCSVArray(CSVId, str(i))
                # Pembuat
                AppendCSVArray(CSVPembuat, username)
                # Bahan-bahan
                AppendCSVArray(CSVPasir, str(pasir))
                AppendCSVArray(CSVBatu, str(batu))
                AppendCSVArray(CSVAir, str(air))

                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: {100 - CSVId.Neff}")
            else:
                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: 0")
    
    return ( CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVJumlah)





