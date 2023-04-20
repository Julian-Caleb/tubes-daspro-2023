# import 
from TipeBentukan import CSVArray
from AdditionalFunction import AppendCSVArray, MinCSVArray, MaxCSVArray, TotalHarga, SumCSVArray

# { PROCEDURE LAPORANCANDI }
# { Procedure LaporanCandi yang hanya dapat dilakukan oleh Bandung Bondowoso (“bandung_bondowoso”) menerima 4 CSV Array dan mengeluarkan pesan-pesan terkait berapa banyak candi yang dibuat, banyak pasir, batu, dan air yang digunakan, serta informasi ID candi termahal dan termurah.
#   I.S. 4 buah CSVArray
#   F.S. Mengeluarkan pesan}

# { KAMUS LOKAL }
# constant Nmax : integer = 103

# type CSVArray : < arr : array [0..Nmax-1] of string,
#				Neff : integer >
	
# CSVId, CSVPasir, CSVBatu, CSVAir : CSVArray
# tempHarga : CSVArray

# totalCandi, totalPasir, totalBatu, totalAir : integer
# hargaMax, hargaMin, idMax, idMin : integer
# indexMax, indexMin : integer
# i : integer

# function SumCSVArray ( CSVArray : CSVArray ) -> integer
# function TotalHarga (pasir : integer, batu : integer, air : integer) -> integer
# function MaxCSVArray (CSVArray : CSVArray) -> integer, integer
# function MinCSVArray (CSVArray : CSVArray) -> integer, integer
# function integer (string : string) -> integer
# { fungsi terdefinisi yang mengubah tipe data string menjadi integer }
# function string (integer : integer) -> string
# { fungsi terdefinisi yang mengubah tipe data integer menjadi string }

# { ALGORITMA }
def LaporanCandi (role : str, CSVId : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray):

    # cek role 
    if (role != "bandung_bondowoso") :

        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

    else : # role == "bandung_bondowoso" 

        # { Inisialisasi variabel }
        totalCandi = 0
        totalPasir = 0 
        totalBatu = 0
        totalAir = 0

        # { mengisi variabel }
        totalCandi = CSVId.Neff
        if (totalCandi == 0):
            print("> Total Candi: 0")
            print("> Total Pasir yang digunakan: 0")
            print("> Total Batu yang digunakan: 0")
            print("> Total Air yang digunakan: 0")
            print("> ID Candi Termahal: -")
            print("> ID Candi Termurah: -")

        else: # { totalCandi > 0 } 
            totalPasir = SumCSVArray(CSVPasir)
            totalBatu = SumCSVArray(CSVBatu)
            totalAir = SumCSVArray(CSVAir)

            # { membuat CSVArray sementara untuk harga }
            Nmax = 103
            tempHarga = CSVArray([None for i in range (Nmax)], 0)
            tempHarga.arr[0] = "MARK"

            # { iterasi menghitung harga total }
            i = 0
            while (CSVId.arr[i] != "MARK"):

                # { cek jika ada isinya }
                if (CSVId.arr[i] != None):

                    # { menghitung harga dan dimasukkan tempHarga }
                    AppendCSVArray(tempHarga, str(TotalHarga(int(CSVPasir.arr[i]), int(CSVBatu.arr[i]), int(CSVAir.arr[i]))))

                else: # { CSVId.arr[i] /= None }

                    AppendCSVArray(tempHarga, None)

                i = i + 1

            # { CSVId.arr[i] = “MARK” }
            (hargaMax, indexMax) = MaxCSVArray(tempHarga)
            (hargaMin, indexMin) = MinCSVArray(tempHarga)
            idMax = CSVId.arr[indexMax]
            idMin = CSVId.arr[indexMin]

            print("> Total Candi:", totalCandi)
            print("> Total Pasir yang digunakan:", totalPasir)
            print("> Total Batu yang digunakan:", totalBatu)
            print("> Total Air yang digunakan:", totalAir)
            print("> ID Candi Termahal:", idMax, "(Rp" + str(hargaMax) + ")")
            print("> ID Candi Termurah:", idMin, "(Rp" + str(hargaMin) + ")")
