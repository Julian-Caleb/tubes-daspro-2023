# import
from TipeBentukan import CSVArray
from AdditionalFunction import Frequency, IndexOf, AmbilBahan, AppendCSVArray, SumCSVArray, MemberOf

# FUNCTION BATCHBANGUN 
# Function BatchBangun, yang hanya bisa dilakukan oleh role bandung_bondowoso, melakukan pembangunan candi oleh setiap jin pembangun yang ada.
# 	I.S. 1 string dan 9 CSVArray
# 	F.S. 6 CSVArray

# KAMUS LOKAL 
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVUsername, CSVRole : CSVArray
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVDeskripsi, CSVJumlah : CSVArray

# jumlahJin : integer
# i, j : integer
# tempPembuatArray, tempPasirArray, tempBatuArray, tempAirArray: CSVArray
# tempPasir, tempBatu, tempAir : integer
# pasir, batu, air : integer

# function Frequency (arr : array [0..Nmax-1] of string, keyword : string) -> integer
# function AppendCSVArray (CSVArray : CSVArray, element : string) -> CSVArray
# function SumCSVArray ( CSVArray : CSVArray ) -> integer
# function AmbilBahan (CSVNama : CSVArray, CSVJumlah : CSVArray, argumen : string) -> integer, integer, integer

# ALGORITMA 
def BatchBangun (role : str, CSVUsername : CSVArray, CSVRole : CSVArray, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray,  CSVNama : CSVArray, CSVJumlah : CSVArray) -> (CSVArray, CSVArray, CSVArray, CSVArray, CSVArray, CSVArray) :
    
    # cek role, jika salah 
    if (role != "bandung_bondowoso") :
        return (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVJumlah)
    
    # jika benar
    else : # role == "bandung_bondowoso" 
        
        # menghitung banyak jin pembangun
        jumlahJin = Frequency(CSVRole.arr, "jin_pembangun")
        
        # kalau jin pembangun 0
        if (jumlahJin == 0) :
            print("Bangun gagal. Anda tidak mempunyai jin pembangun. Silahkan summon terlebih dahulu.")
        
        # kalau jin pembangun lebih dari 0
        else : # (jumlahJin > 0)
            
            # inisialisasi variabel
            Nmax = 103
            tempPembuatArray = CSVArray([None for i in range (Nmax)], 0)
            tempPembuatArray.arr[0] = "MARK"
            tempPasirArray = CSVArray([None for i in range (Nmax)], 0)
            tempPasirArray.arr[0] = "MARK"
            tempBatuArray = CSVArray([None for i in range (Nmax)], 0)
            tempBatuArray.arr[0] = "MARK"
            tempAirArray = CSVArray([None for i in range (Nmax)], 0)
            tempAirArray.arr[0] = "MARK"
            banyakPasir = 0
            banyakBatu = 0
            banyakAir = 0
            
            # iterasi
            i = 0
            
            while (i < CSVRole.Neff) :
                
                # cek jin pembangun
                if (CSVRole.arr[i] == "jin_pembangun") :
                                        
                    # randomize bahan, pastikan tidak ada yang 0
                    while True :
                        (tempPasir, tempBatu, tempAir) = AmbilBahan(CSVNama, CSVJumlah, "random")
                        if (tempPasir > 0) and (tempBatu > 0) and (tempAir > 0) :
                            break
                    
                    # bahan dan username dimasukkan ke temporary (CSVArray) 
                    AppendCSVArray (tempPembuatArray, CSVUsername.arr[i])
                    AppendCSVArray (tempPasirArray, str(tempPasir))
                    AppendCSVArray (tempBatuArray, str(tempBatu))
                    AppendCSVArray (tempAirArray, str(tempAir))
                    
                i = i + 1
            
            # keluarkan pesan 
            print("Mengerahkan", jumlahJin, "jin untuk membangun candi dengan total bahan", SumCSVArray (tempPasirArray), "pasir,", SumCSVArray (tempBatuArray), "batu, dan", SumCSVArray (tempAirArray), "air.")

            # cek apakah bahan cukup atau tidak
            (pasir, batu, air) = AmbilBahan (CSVNama, CSVJumlah, "data")
            
            # Jika cukup,           
            if (SumCSVArray (tempPasirArray) <= pasir) and (SumCSVArray (tempBatuArray) <= batu) and (SumCSVArray (tempAirArray) <= air) :

                # iterasi array temporary dimasukkan ke dalam CSVArray, perhatikan tipe data 
                i = 0
                while (i < tempPembuatArray.Neff) :
                    
                    # mencari id yang available antara 1 sampai 100}
                    j = 1
                    
                    while (MemberOf(CSVId.arr, str(j))) :
                        j = j + 1
                        
                    # asumsikan jika id > 100, tidak dimasukkan array. 
                    if ( j < 100 ) :
                        
                        # id 
                        AppendCSVArray(CSVId, str(j))

                        # pembuat 
                        AppendCSVArray(CSVPembuat, tempPembuatArray.arr[i])

                        # bahan-bahan 
                        AppendCSVArray(CSVPasir, tempPasirArray.arr[i])
                        AppendCSVArray(CSVBatu, tempBatuArray.arr[i])
                        AppendCSVArray(CSVAir, tempAirArray.arr[i])
            
                    i += 1
                
                # mengurangi database 
                CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")] = str(pasir - SumCSVArray (tempPasirArray))
                CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")] = str(batu - SumCSVArray (tempBatuArray))
                CSVJumlah.arr[IndexOf(CSVNama.arr, "air")] = str(air - SumCSVArray (tempAirArray))
            
                # tampilkan pesan 
                print ("Jin berhasil membangun total", tempPembuatArray.Neff, "candi.")
                
            else : # (SumCSVArray (tempPasirArray) > pasir) or (SumCSVArray (tempBatuArray) > batu) or (SumCSVArray (tempAirArray) > air)
                
                # keluarkan pesan 
                print("Bangun gagal. Kurang ", end ="")
                if (SumCSVArray (tempPasirArray) > pasir) :
                    print(SumCSVArray (tempPasirArray) - pasir, "pasir", end ="")
                    if (SumCSVArray (tempBatuArray) > batu) and (SumCSVArray (tempAirArray) > air) :
                        print(",", end= " ")
                    elif (SumCSVArray (tempBatuArray) > batu) or (SumCSVArray (tempAirArray) > air) :
                        print(" dan", end= " ")
                    else : # (SumCSVArray (tempBatuArray) < batu) and (SumCSVArray (tempAirArray) < air)
                        print(".")
                if (SumCSVArray (tempBatuArray) > batu) :
                    print (SumCSVArray (tempBatuArray) - batu, "batu", end = "")
                    if (SumCSVArray (tempPasirArray) > pasir) and (SumCSVArray (tempAirArray) > air) :
                        print(", dan", end= " ")
                    elif (SumCSVArray (tempAirArray) > air) : 
                        print(" dan", end= " ")
                    else : # (SumCSVArray (tempPasirArray) < pasir) and (SumCSVArray (tempAirArray) < air)
                        print(".")
                if (SumCSVArray (tempAirArray) > air) :
                    print(SumCSVArray (tempAirArray) - air, "air.")
                
            return (CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVJumlah)

#-----------------------------------------------------------------------------------#

# FUNCTION BATCHKUMPUL 
# Function BatchKumpul, yang hanya bisa dilakukan oleh role bandung_bondowoso, melakukan pengumpulan bahan-bahan bangunan yaitu pasir, batu, dan air, dengan menggunakan randomizer yang menghasilkan bahan dari 0-5.
# I.S. 1 string untuk validasi dan 3 buah CSVArray 
# F.S. 1 buah CSVArray dengan modifikasi banyak batu, pasir, dan air

# KAMUS LOKAL 
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

# ALGORITMA 
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
    print("Jin menemukan total", pasir, "pasir,", batu, "batu, dan", air, "air.")

    # menjumlahkan ke database 
    CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")]) + pasir)
    CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")]) + batu)
    CSVJumlah.arr[IndexOf(CSVNama.arr, "air")] = str(int(CSVJumlah.arr[IndexOf(CSVNama.arr, "air")]) + air)

    return (CSVJumlah)
