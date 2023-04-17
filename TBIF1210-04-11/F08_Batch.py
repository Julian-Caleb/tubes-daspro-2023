# import
from TipeBentukan import CSVArray
from AdditionalFunction import Frequency, IndexOf, AmbilBahan

# { FUNCTION BATCHKUMPUL }
# { Function BatchKumpul, yang hanya bisa dilakukan oleh role bandung_bondowoso, melakukan pengumpulan bahan-bahan bangunan yaitu pasir, batu, dan air, dengan menggunakan randomizer yang menghasilkan bahan dari 0-5.
# I.S. 1 string untuk validasi dan 3 buah CSVArray 
# F.S. 1 buah CSVArray dengan modifikasi banyak batu, pasir, dan air} 
# { KAMUS LOKAL }
# constant Nmax : integer = 103
# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVNama, CSVJumlah : CSVArray

# role : string
# jumlahJin : integer
# tempPasir, tempBatu, tempAir : integer
# pasir, batu, air : integer

# function Frequency (arr : array [0..Nmax-1] of string, keyword : string) -> integer
# function IndexOf (arr : array [0..Nmax-1] of string, keyword : string) -> integer
# function AmbilBahan (CSVNama : CSVArray, CSVJumlah : CSVArray, argumen : string) -> integer, integer, integer

# { ALGORITMA }
def BatchKumpul (role : str, CSVRole : CSVArray, CSVNama : CSVArray, CSVJumlah : CSVArray) -> CSVArray :

    # cek role 
    if (role != "bandung_bondowoso") :
        return (CSVJumlah)

    else : # role = “bandung_bondowoso” 
        
        # inisialisasi 
        pasir = 0 
        batu = 0
        air = 0

    # menghitung banyak jin_pengumpul 
    jumlahJin = Frequency(CSVRole.arr, "jin_pengumpul")

    # jika tidak ada jin pengumpul 
    if (jumlahJin == 0) :
        print ("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

    # iterasi sebanyak jumlah jin pengumpul 
    for i in range (jumlahJin) :

        # randomize bahan bangunan yang dibutuhkan oleh candi }
        (tempPasir, tempBatu, tempAir) = AmbilBahan (CSVNama, CSVJumlah, "random")
        pasir = pasir + tempPasir
        batu = batu + tempBatu
        air = air + tempAir

    # kirim pesan 
    print("Mengerahkan", jumlahJin, "jin untuk mengumpulkan bahan.")
    print("Jin menemukan total", pasir, "pasir,", batu, "batu, dan ", air, "air.")

    # menjumlahkan ke database 
    CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")]) + pasir)
    CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")]) + batu)
    CSVJumlah.arr[IndexOf(CSVNama.arr, "air")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "air")]) + air)

    return (CSVJumlah)
