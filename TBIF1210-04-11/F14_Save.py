# { PROCEDURE SAVE }
# { Procedure Save menerima 11 CSVArray, meminta input nama folder dari user, membuat folder tersebut jika tidak tersedia, membuat 3 buah file csv, dan menuliskan data pada CSVArray ke dalam file-file csv tersebut. 
# I.S. 11 buah CSVArray
# F.S. Memasukkan CSVArray ke dalam 3 file CSV }

# { KAMUS LOKAL }
# constant Nmax : integer = 103
# constant mark : string = “”

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
	
# CSVUSername, CSVPassword, CSVRole : CSVArray
# CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir : CSVArray
# CSVNama, CSVDeskripsi, CSVJumlah : CSVArray

# file : SEQFILE of
# (*) baris : string
# (1) mark
	
# namaFolder : string
# csvPath : string

# function os.path.exists (namaFolder : string) -> Boolean
# { fungsi terdefinisi yang mengecek apakah terdapat folder namaFolder dalam folder program berada }
# procedure os.mkdir (input namaFolder : string)
# { prosedur terdefinisi yang membuat folder namaFolder }
# function os.path.join(namaFolder1 : string, namaFolder2 : string) -> string
# { fungsi terdefinisi yang menyatukan beberapa string menjadi path folder }

# ALGORITMA 
# Import
import os
from TipeBentukan import CSVArray

def Save (CSVUsername : CSVArray, CSVPassword : CSVArray, CSVRole : CSVArray, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray, CSVNama : CSVArray, CSVDeskripsi : CSVArray, CSVJumlah : CSVArray) :

    namaFolder = input("Masukkan nama folder: ")

    # Cek jika folder save ada atau belum
    # Jika tidak ada,
    if not os.path.exists("save"):
        os.mkdir("save")
        print("Membuat folder save...")

    # Cek jika folder input sudah ada atau belum
    # Jika tidak ada,
    if not os.path.exists(os.path.join("save", namaFolder)):
        os.mkdir(os.path.join("save", namaFolder))
        print("Membuat folder save/" + namaFolder + "...")

    # Memasukkan ke dalam file csv
    # 1. user.csv
    csvPath = os.path.join("save", namaFolder, "user.csv")

    # Mengisi file csv
    with open(csvPath, "w") as file:
        i = 0
        file.write("username;password;role\n")
        while (CSVUsername.arr[i] != "MARK") and (CSVPassword.arr[i] != "MARK") and (CSVRole.arr[i] != "MARK") :
            if (CSVUsername.arr[i] != None) :
                file.write(CSVUsername.arr[i])
                file.write(";")
                file.write(CSVPassword.arr[i])
                file.write(";")
                file.write(CSVRole.arr[i])
                file.write("\n")
            i += 1
    
    # menutup file    
    file.close()
            
    # 2. candi.csv
    csvPath = os.path.join("save", namaFolder, "candi.csv")

    # Mengisi file csv
    with open(csvPath, "w") as file:
        i = 0
        file.write("id;pembuat;pasir;batu;air\n")
        while (CSVId.arr[i] != "MARK") and (CSVPembuat.arr[i] != "MARK") and (CSVPasir.arr[i] != "MARK") and (CSVBatu.arr[i] != "MARK") and (CSVAir.arr[i] != "MARK") :
            if (CSVId.arr[i] != None) :
                file.write(CSVId.arr[i])
                file.write(";")
                file.write(CSVPembuat.arr[i])
                file.write(";")
                file.write(CSVPasir.arr[i])
                file.write(";")
                file.write(CSVBatu.arr[i])
                file.write(";")
                file.write(CSVAir.arr[i])
                file.write("\n")
            i += 1
    
    # menutup file    
    file.close()
    
    # 3. bahan_bangunan.csv
    csvPath = os.path.join("save", namaFolder, "bahan_bangunan.csv")

    # Mengisi file csv
    with open(csvPath, "w") as file:
        i = 0
        file.write("nama;deskripsi;jumlah\n")
        while (CSVNama.arr[i] != "MARK") and (CSVDeskripsi.arr[i] != "MARK") and (CSVJumlah.arr[i] != "MARK") :
            if (CSVNama.arr[i] != None) :
                file.write(CSVNama.arr[i])
                file.write(";")
                file.write(CSVDeskripsi.arr[i])
                file.write(";")
                file.write(CSVJumlah.arr[i])
                file.write("\n")
            i += 1
    
    # menutup file    
    file.close()

    print("Berhasil menyimpan data di folder save/" + namaFolder + "!")
