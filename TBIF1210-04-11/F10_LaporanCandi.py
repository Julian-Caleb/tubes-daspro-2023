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
def LaporanCandi (input CSVId : CSVArray, input CSVPasir : CSVArray, input CSVBatu : CSVArray, input CSVAir : CSVArray):

    # { Inisialisasi variabel }
    totalCandi, totalPasir, totalBatu, totalAir = 0

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
    tempHarga.arr = ['MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    tempHarga.Neff = 0

    # { iterasi menghitung harga total }
    i = 0
    while (CSVId.arr[i] != "MARK"):

        # { cek jika ada isinya }
        if (CSVId.arr[i] != None):

            # { menghitung harga dan dimasukkan tempHarga }
            AppendCSVArray(tempHarga, string(TotalHarga(integer(CSVPasir.arr[i]), integer(CSVBatu.arr[i]), integer(CSVAir.arr[i])))

        else: # { CSVId.arr[i] /= None }

            AppendCSVArray(tempHarga, None)

        i = i + 1

    # { CSVId.arr[i] = “MARK” }
    hargaMax, indexMax = MaxCSVArray(tempHarga)
    hargaMin, indexMin = MinCSVArray(tempHarga)
    idMax = CSVId.arr[indexMax]
    idMin = CSVId.arr[indexMin]

    print("> Total Candi: ", totalCandi)
    print("> Total Pasir yang digunakan: ", totalPasir)
    print("> Total Batu yang digunakan: ", totalBatu)
    print("> Total Air yang digunakan: ", totalAir)
    print("> ID Candi Termahal: ", idMax, "(Rp ", hargaMax, ")")
    print("> ID Candi Termurah: ", idMin, "(Rp ", hargaMin, ")")
