# import function
from TipeBentukan import CSVArray
from AdditionalFunction import Frequency, AppendCSVArray, MaxCSVArray, MinCSVArray, CompareArrayOfString, AmbilBahan

# FUNCTION LAPORANJIN
# Fungsi LaporanJin yang hanya dapat dilakukan oleh Bandung Bondowoso (“bandung_bondowoso”) menerima 5 CSV Array dan mengeluarkan pesan-pesan terkait jumlah jin, jin terajin dan termalas, serta banyak pasir, batu, dan array yang dimiliki.
# I.S. 5 buah CSVArray
# F.S. Mengeluarkan pesan

# KAMUS LOKAL
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string, Neff : integer >

# CSVUsername, CSVRole, CSVPembuat, CSVNama, CSVJumlah : CSVArray
# tempBanyakCandi, tempJin : CSVArray

# nilaiMax, nilaiMin, indexMax, indexMin : integer
# jumlahJin, i : integer
# jinTerajin, jinTermalas : string

# function Frequency (arr : List, keyword : string) -> integer
# function AppendCSVArray (CSVArray : CSVArray, element : string) -> CSVArray
# function MaxCSVArray (CSVArray : CSVArray) -> integer, integer
# function MinCSVArray (CSVArray : CSVArray) -> integer, integer
# function CompareArrayOfString (arr : List, op : string) -> string
# function string (integer : integer) -> string
# { fungsi terdefinisi yang mengubah tipe data integer menjadi string }
# function integer (string : string) -> integer
# { fungsi terdefinisi yang mengubah tipe data string menjadi integer }

# ALGORITMA
def LaporanJin(role : str, CSVUsername : CSVArray, CSVRole : CSVArray, CSVPembuat : CSVArray, CSVNama : CSVArray, CSVJumlah : CSVArray) : 
    
    # cek role 
    if (role != "bandung_bondowoso") :

        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

    else : # role == "bandung_bondowoso"

        # inisialisasi variabel
        Nmax = 103
        pasir = 0
        batu = 0
        air = 0
        
        # Menghitung jumlah jin terlebih dahulu
        jumlahJin = Frequency(CSVRole.arr, "jin_pengumpul") + Frequency(CSVRole.arr, "jin_pembangun")
        
        # inisiasi variabel untuk mencari jin terajin dan termalas
        tempBanyakCandi = CSVArray([None for i in range (Nmax)], 0)
        tempBanyakCandi.arr[0] = "MARK"
        
        i = 0
        
        # iterasi untuk mengisi tempBanyakCandi
        while (CSVRole.arr[i] != "MARK"):
            
            # Kalau ada isinya
            if (CSVRole.arr[i] != None):
                
                # menghitung banyak candi dan dimasukkan tempBanyakCandi
                AppendCSVArray(tempBanyakCandi, str(Frequency(CSVPembuat.arr, CSVUsername.arr[i])))
                
            else:
                AppendCSVArray(tempBanyakCandi, None)
                
            i = i + 1
        
        # mencari jinTerajin
        (nilaiMax, indexMax) = MaxCSVArray(tempBanyakCandi)  
        
        # Cek ada lebih dari satu atau tidak
        # jika tidak ada
        if Frequency(tempBanyakCandi.arr, str(nilaiMax)) == 0:
            jinTerajin = "-"
        
        # jika hanya 1
        elif Frequency(tempBanyakCandi.arr, str(nilaiMax)) == 1:
            jinTerajin = CSVUsername.arr[indexMax]
        
        # Jika lebih dari 1
        else: # Frequency(tempBanyakCandi.arr, str(nilaiMax)) > 1
            tempJin = CSVArray([None for i in range (Nmax)], 0)
            tempJin.arr[0] = "MARK"
            
            # melakukan iterasi
            i = 0
            while (tempBanyakCandi.arr[i] != "MARK") :
                
                if (int(tempBanyakCandi.arr[i]) == nilaiMax) :
                    AppendCSVArray(tempJin, CSVUsername.arr[i])
            
                i += 1
            
            # cek leksikografis tertinggi
            jinTerajin = CompareArrayOfString(tempJin.arr, "<")

        # mencari jinTermalas
        (nilaiMin, indexMin) = MaxCSVArray(tempBanyakCandi)
        
        # Cek ada lebih dari satu atau tidak
        # jika tidak ada
        if Frequency(tempBanyakCandi.arr, str(nilaiMin)) == 0:
            jinTermalas = "-"
        
        # jika hanya 1
        elif Frequency(tempBanyakCandi.arr, str(nilaiMin)) == 1 :
            jinTermalas = CSVUsername.arr[indexMin]
        
        # Jika lebih dari 1
        else: # Frequency(tempBanyakCandi.arr, str(nilaiMin)) > 1
            tempJin = CSVArray([None for i in range (Nmax)], 0)
            tempJin.arr[0] = "MARK"
            
            # melakukan iterasi
            i = 0
            while (tempBanyakCandi.arr[i] != "MARK"):
                
                # filter hanya jin pembangun
                if (CSVRole.arr[i] == "jin_pembangun") and (int(tempBanyakCandi.arr[i]) == nilaiMin):
                    AppendCSVArray(tempJin, CSVUsername.arr[i])
            
                i += 1
            
            # cek leksikografis tertinggi
            jinTermalas = CompareArrayOfString(tempJin.arr, "<")
            
            # mengambil data batu, pasir, air
            (pasir, batu, air) = AmbilBahan(CSVNama, CSVJumlah, "data")            
            
        # print pesan
        print("> Total Jin:", jumlahJin)
        print("> Total Jin Pengumpul:", Frequency (CSVRole.arr, "jin_pengumpul"))
        print("> Total Jin Pembangun:", Frequency (CSVRole.arr, "jin_pembangun"))
        print("> Jin Terajin:", jinTerajin)
        print("> Jin Termalas:", jinTermalas)
        print("> Jumlah Pasir:", pasir , "unit")
        print("> Jumlah Batu:", batu, "unit")
        print("> Jumlah Air:", air, "unit")
    
    

   


    
                   