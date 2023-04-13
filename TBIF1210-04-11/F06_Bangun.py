from CSVParser import CSVParser
from typing import List
from TipeBentukan import CSVArray
from AdditionalFunction import MemberOf, IndexOf, Delete, Length, LengthArray, Append
from BonusFunction import Lcg_rng

# FUNCTION BANGUN
# Function bangun, yang hanya dapat dilakukan oleh user dengan role jin_pembangun, bertugas untuk membangun candi berdasarkan bahan bangunan yang di randomize (jika bahan cukup, candi dibangun, jika tidak, batal dibangun). Maksimal candi yang dapat dibangun adalah 100 candi, jika lebih maka tidak disimpan. 
#   I.S. 2 string dan 7 CSVArray
#   F.S. 7 CSVArray yang mungkin sudah dimodifikasi berdasarkan candi yang dibangun dan bahan bangunan yang digunakan

# KAMUS LOKAL

# 	constant Nmax : integer = 103

# username, password, role : string
# pasir, batu, air : integer 
# banyakPasir, banyakBatu, banyakAir : integer
# i : integer

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVDeskripsi, CSVJumlah : CSVArray

# function IndexOf (arr : array [0..Nmax-1] of string, keyword : string) -> integer
# function AppendCSVArray (CSVArray : CSVArray, element : string) -> CSVArray
# function lcg_rng () -> integer

def Bangun (role : str, CSVUsername : CSVArray, CSVPassword : CSVArray, CSVRole : CSVArray, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray) :

    # Mengecek apakah (role) diisi dengan "jin_pembangun"
    # Jika tidak
    if role != "jin_pembangun":
        return (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)
    
    else:
        # Bahan yang dibutuhkan untuk membuat candi
        pasir = Lcg_rng()
        batu = Lcg_rng()
        air = Lcg_rng()

        # Cek bahan yang dimiliki
        banyakPasir = IndexOf(CSVPasir.arr, "pasir")
        banyakBatu = IndexOf(CSVBatu.arr, "batu")
        banyakAir = IndexOf(CSVAir.arr, "air")

        # Jika bahan tidak mencukupi
        if pasir > banyakPasir or batu > banyakBatu or air > banyakAir:
            print("Bahan bangunan tidak mencukupi")
            print("Candi tidak bisa dibangun!")
        else:
            # Mengurangi bahan yang dimiliki
            banyakPasir = banyakPasir - pasir
            banyakBatu = banyakBatu - batu
            banyakAir = banyakAir - air

            # Masukkan kembali ke array
            CSVPasir = banyakPasir
            CSVBatu = banyakBatu
            CSVAir = banyakAir

            # Mencari id yang available antara 1 sampai 100
            i = 1
            while MemberOf(CSVId, i):
                i = i +1
            
            if i < 101:
                # id
                Append(CSVId, i)
                # Pembuat
                Append(CSVPembuat, "username")
                # Bahan-bahan
                Append(CSVPasir, pasir)
                Append(CSVBatu, batu)
                Append(CSVAir, air)

                print("Candi berhasil dibangun")
                print(f"Sisa candi yang perlu dibangun: {100-i}")
            else:
                print("Candi berhasil dibangun")
                print(f"Sisa candi yang perlu dibangun: 0")
    
        return (CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir)





