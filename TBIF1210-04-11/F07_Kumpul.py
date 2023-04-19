from TipeBentukan import CSVArray
from AdditionalFunction import AmbilBahan, IndexOf

# FUNCTION KUMPUL
# Function Kumpul, yang hanya bisa dilakukan oleh jin dengan role jin_pengumpul, bertugas untuk mengumpulkan bahan-bahan bangunan yaitu pasir, batu, dan air, dengan menggunakan randomizer yang menghasilkan bahan dari 0-5
#   I.S. 1 string untuk validasi dan 2 buah CSVArray
#   F.S. 1 buah CSVArray

# KAMUS LOKAL
# constant Nmax : integer = 103
# type CSVArray : <arr : array [0..Nmax-1] of string, Neff : integer >
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVJumlah : CSVArray

# role : string
# pasir, batu, air : integer

# function IndexOf (arr : List, keyword : string) -> integer
# function AmbilBahan (CSVNama : CSVArray, CSVJumlah : CSVArray, argumen : string) -> (integer, integer, integer)

def Kumpul (role : str, CSVNama : CSVArray, CSVJumlah : CSVArray) -> (CSVArray):
   
   
    # Mengecek apakah (role) diisi dengan "jin_pembangun"
    # Jika tidak
    if role != "jin_pengumpul":
        return CSVJumlah
    
    # Jika ya, randomize bahan bangunan yang dibutuhkan oleh candi
    else:
        pasir, batu, air = AmbilBahan (CSVNama, CSVJumlah, "random")
        print(str(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air."))
    
    CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")]) + pasir)
    CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")]) + batu)
    CSVJumlah.arr[IndexOf(CSVNama.arr, "air")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "air")]) + air)
    
    return CSVJumlah
