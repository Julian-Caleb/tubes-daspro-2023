# Import
from typing import List
from TipeBentukan import CSVArray
from BonusFunction import Lcg_rng

#-----------------------------------------------------------------------------------#
# FUNCTION LENGTHARRAY 
# Fungsi LengthArray menerima sebuah array dan mengembalikan banyak elemen efektif dari indeks 0 hingga elemen sebelum MARK 
# Menggunakan rekursif dengan basis arr[i] == "MARK" mengembalikan nilai 0 dan rekursi arr[i] /= "MARK" mengembalikan 1 + LengthArray(arr,i+1)
#   I.S. Sebuah array yang mengandung MARK
#   F.S. Banyak elemen efektif 

# KAMUS LOKAL 
# constant Nmax : int = 103
# type List: array [0..Nmax-1] of str
# i, count : int

# ALGORITMA 
def LengthArray (arr: List, i : int = 0) -> int :
    
    # rekursif
    if arr[i] == "MARK" : # basis
        return 0
    else : # rekursi, arr[i] != "MARK"
        return 1 + LengthArray(arr,i+1)


# APLIKASI
# print(LengthArray(['Bondowoso', 'Roro', 'Lmao', 'MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]))

#-----------------------------------------------------------------------------------#

# FUNCTION LENGTHSTRING
# Fungsi LengthString menerima sebuah string dan mengembalikan jumlah huruf dalam string
#   I.S. Sebuah string 
#   F.S. Banyak huruf dalam string

# KAMUS LOKAL 
# type str: string
# i, count : integer

# ALGORITMA 
def LengthString (string : str) -> int : 
    return len(string)
    
# APLIKASI
# print(Length("Easter Egg"))

#-----------------------------------------------------------------------------------#

# FUNCTION LENGTHCSV
# Fungsi LengthCSV menerima sebuah array (khusus pengolahan data dari csv) dan mengembalikan jumlah elemen dalam array 
#     I.S. Sebuah array dari CSV
#     F.S. Banyak elemen dalam array 

# KAMUS LOKAL 
# constant Nmax : integer = 10
# type List : array [0..Nmax] of string { berisi data raw dari CSV }
# i, count : integer

# ALGORITMA 
def LengthCSV (arr : List) -> int : 
    return len(arr)

#-----------------------------------------------------------------------------------#

# FUNCTION SPLIT 
# Function split menerima 3 buah masukan yaitu sebuah string, array sebagai template hasil pemisahan, dan character yang menjadi penanda dilakukannya pemisahan
#   I.S. 1 string, 1 array, dan 1 char
#   F.S. array yang berisi hasil pemisahan 

# KAMUS LOKAL 
# type List : array of string

# split : string
# result : List
# splitter : char

# temp : string
# i : integer

# function LengthString (str : string) -> integer
# function Append (arr : List, element : string) -> List

# ALGORITMA
def Split (split : str, result : List, splitter : str) -> List :
    temp = ""
    i = 0
    while (i < LengthString(split)) and split[i] != None :
        if split[i] != splitter :
            temp += split[i]
        else :
            Append(result, temp)
            temp = ""
        i += 1
    if temp != "" :
        Append(result, temp)
    
    return result

#-----------------------------------------------------------------------------------#

# FUNCTION APPEND 
# Fungsi Append menerima sebuah array dan string, menambahkan string pada array dan menambahkan 1 pada array.
#   I.S. sebuah array of string dan element
#   F.S. array gabungan array lama dan element tersebut 

# KAMUS LOKAL 

# constant Nmax : integer = 103
# type List : array [0..Nmax-1] of string
# arr : List
# i : integer

# ALGORITMA
def Append (arr : List, element : str) -> List :

    # inisialisasi variabel 
    i = 0

    # elemen akan dimasukkan pada elemen yang kosong pada array (None) atau di paling belakang (menggeser array) dengan asumsi pasti ada “MARK” 

    # iterasi hingga menemukan None atau “MARK” dengan skema search
    while (arr[i] != None) and (arr[i] != "MARK") :
        i = i + 1 

    # memasukkan dan menggeser
    if (arr[i] == None) :
        arr[i] = element
        
    else : # arr[i] = “MARK” 
        arr[i] = element
        arr[i+1] = "MARK"
    return arr

#-----------------------------------------------------------------------------------#

# FUNCTION APPENDCSVARRAY 
# Fungsi AppendCSVArray menerima sebuah CSVarray dan string, menambahkan string pada CSVarray.arr dan menambahkan 1 pada CSVArray.Neff.
#   I.S. sebuah CSVArray dan element
#   F.S. CSVArray dengan CSVArray.arr gabungan array lama dan element tersebut serta CSVArray.Neff yang telah ditambah 1

# KAMUS LOKAL
# constant Nmax : integer = 103
# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# i : integer

# ALGORITMA 
def AppendCSVArray (CSVArray : CSVArray, element : str) -> CSVArray :

    # melakukan append pada array 
    Append(CSVArray.arr, element)

    # menambahkan 1 elemen pada Neff 
    CSVArray.Neff = CSVArray.Neff + 1

    return CSVArray

#-----------------------------------------------------------------------------------#

# FUNCTION ORDCHAR 
# Function OrdChar menerima sebuah input sebuah karakter dan mengembalikan nilai (leksikografis) berdasarkan urutan alfabet referensi
# Menggunakan rekursif dengan basis jika x = alphabet[i] mengembalikan i + 1, dan rekursi jika x /= alphabet[i] mengembalikan OrdChar (x, i+1) 
#   I.S. sebuah char
#   F.S. integer urutan ke berapa karakter tersebut berada 

# KAMUS LOKAL 
# x : char
# alfabet : string
# index : integer

# ALGORITMA
def OrdChar (x : str, i : int = 0) -> int :
    
    # asumsikan pasti ketemu
    # inisialisasi variabel
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if x == alphabet[i] : # basis
        return i + 1
    else : # rekursif, x != alphabet[i]
        return OrdChar(x, i + 1)
    
# APLIKASI
# print(OrdChar("z"))

#-----------------------------------------------------------------------------------#

# FUNCTION COMPARESTRING
# Function CompareString dibuat untuk menerima input 2 string dan operator (> atau <).
# membandingkan leksikografis antara 2 string, mengembalikan string
# dengan leksikografis lebih tinggi atau rendah berdasarkan operatornya
#   I.S. 2 buah string dan pembandingnya
#   F.S. string yang lebih kecil atau besar leksikografisnya

# KAMUS 
# charIndex : integer
# stringOne, stringTwo, op : string

# function OrdChar (x : char) -> integer

# ALGORITMA
def CompareString (stringOne : str, stringTwo : str, op : int) -> str : 
    # asumsi kedua string pasti berbeda dan perbandingan hanya lebih besar atau lebih kecil
    
    # charIndex sebagai penanda huruf keberapa
    charIndex = 0
    
    # mencari huruf yang berbeda pada kedua string untuk charIndex yang sama
    while OrdChar(stringOne[charIndex]) == OrdChar(stringTwo[charIndex]) :
        charIndex += 1
        
    # berdasarkan operatornya, 
    if op == ">" :
        if OrdChar(stringOne[charIndex]) > OrdChar(stringTwo[charIndex]) :
            return stringOne # leksikografis lebih tinggi
        else :
            return stringTwo
    else :  # op == "<"
        if OrdChar(stringOne[charIndex]) < OrdChar(stringTwo[charIndex]) :
            return stringOne # leksigorafis lebih rendah
        else :
            return stringTwo
        

#-----------------------------------------------------------------------------------#

# FUNCTION COMPAREARRAYOFSTRING 
# Function CompareArrayOfString menerima array of string dan operator dan mengembalikan string dengan leksikografis tertinggi / terendah berdasarkan operatornya
#   I.S. array of string dan sebuah karakter
#   F.S. string dengan leksikografis tertinggi atau terendah

# KAMUS LOKAL 
# constant Nmax : integer = 103
# type List : array [0..Nmax-1] of string
# arr : List

# op : char
# output : string
# n : integer

# function CompareString (stringOne : string, stringTwo : string, op : char) -> string 
# function LengthArray (arr : List) -> integer

# ALGORITMA
def CompareArrayOfString (arr : List, op : str) -> str :
    output = arr[0]
    n = 1
    while n < LengthArray(arr) and arr[n] != "MARK" :
        output = CompareString (output, arr[n], op)
        n += 1
    return output

# APLIKASI
# print(CompareArrayOfString(["Joni", "Joli", "Jarum", "MARK"], "<"))

#-----------------------------------------------------------------------------------#

# FUNCTION INDEXOF 
# function IndexOf menerima input sebuah array of string dan sebuah keyword string, mencari pada index keberapa string tersebut berada pada array (membaca index pertama kali string tersebut muncul) dan mengembalikan index tersebut. Asumsi string pasti ditemukan (dikarenakan pemanggilan MemberOf sebelum IndexOf).
# Menggunakan rekursi dengan basis jika arr[i] = keyword mengembalikan i dan rekursi jika arr[i] /= keyword mengembalikan IndexOf(arr, keyword, i+1)    
#	I.S. sebuah array of string dan sebuah string
#	F.S. integer index keberapa string tersebut (pertama kali) muncul pada array 

# KAMUS LOKAL 
# constant NMax : int = 103
# type List : array [0..Nmax-1] of str
# arr : List
# keyword : str
# i : int

# ALGORITMA
def IndexOf (arr : List, keyword : str, i : int = 0) -> int :

    if arr[i] == keyword : # basis
        return i
    else : # rekursi, arr[i] != keyword
        return IndexOf(arr, keyword, i + 1)

# APLIKASI
# print(IndexOf(["a","b","c","d","e"], "d"))

#-----------------------------------------------------------------------------------#

# FUNCTION MEMBEROF 
# function MemberOf menerima input sebuah array of string dan sebuah keyword string, mencari apakah string keyword berada pada array dan mengembalikan boolean, True jika ada dan False jika tidak. 
#	I.S. sebuah array of string dan sebuah string
#	F.S. boolean, True jika ditemukan, False jika tidak.

# KAMUS LOKAL 
# constant NMax : int = 103
# type List : array [0..Nmax-1] of str
# arr : List
# keyword : str
# Found : bool
# i : int 

# ALGORITMA 
def MemberOf (arr: List, keyword : str, i : int = 0) -> bool :
    
    # inisialisasi iterasi
    Nmax = 103
    i = 0
    Found = False
    
    # iterasi dilakukan hingga keyword ditemukan atau i = Nmax - 1
    while (i < Nmax-1) and (arr[i] != keyword) :
        i += 1
        
    # i = Nmax-1 or arr[i] == keyword 
    if (arr[i] == keyword) :
        Found = True
    
    return Found

# APLIKASI
# print(MemberOf(['bandung_bondowoso', 'roro_jonggrang', 'MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
# None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], "MARK"))

#-----------------------------------------------------------------------------------#

# FUNCTION FREQUENCY
# Function Frequency menerima sebuah array of string dan keyword string dan mencari berapa kali kemunculan keyword tersebut dalam string.
# Menggunakan rekursi dengan basis jika i = 103 atau i = "MARK" mengembalikan 0, rekursi arr[i] = keyword mengembalikan 1 + Frequency(arr, keyword, i + 1), dan rekursi jika arr[i] /= keyword mengembalikan Frequency(arr, keyword, i + 1)
#   I.S. sebuah array of string dan sebuah string 
#   F.S. integer banyak kemunculan string tersebut dalam array 

# KAMUS LOKAL 
# constant Nmax : int = 103
# type List : array [0..Nmax-1] of str
# arr : List
# keyword : str
# i, count : int

# ALGORITMA 
def Frequency (arr : List, keyword : str, i : int = 0) -> int : 
 
    if i == 103 or arr[i] == "MARK": # basis 
        return 0
    elif arr[i] == keyword : # rekursi 1
        return 1 + Frequency(arr, keyword, i + 1)
    else : # rekursi 2, arr[i] /= keyword
        return Frequency(arr, keyword, i + 1)

# APLIKASI
# print(Frequency(['bandung_bondowoso', 'roro_jonggrang', 'MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
# None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], None))

#-----------------------------------------------------------------------------------#

# FUNCTION DELETE 
# Fungsi Delete menerima sebuah array dan integer index yang akan dihapus dan mengembalikan array. 
#   I.S. array [0..Nmax-1] dan index yang valid, yaitu berada di antara [0..Nmax-1] 
#   F.S. array yang sama namun dengan array[index] (berdasarkan parameter) tidak berisi / berisi None 

# KAMUS LOKAL
# constant Nmax : int = 103
# type List : array [0..Nmax-1] of str
# arr : List

# ALGORITMA
def Delete (arr : List, index : int) -> List :
    
    # membuat arr[index] menjadi None
    arr[index] = None
    
    return arr

# APLIKASI
# print(Delete(['bandung_bondowoso', 'roro_jonggrang', 'MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
#                  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 1))

#-----------------------------------------------------------------------------------#

# FUNCTION DELETECSVARRAY 
# Fungsi DeleteCSVArray menerima sebuah CSVArray index yang akan dihapus dan mengembalikan CSVArray. 
#   I.S. CSVArray dan index yang valid, yaitu berada di antara [0..Nmax-1] 
#   F.S. CSVArray yang sama namun dengan CSVArray[index] (berdasarkan parameter) tidak berisi / berisi None 

# KAMUS LOKAL 
# 	constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >

# function Delete (arr : List, index : integer) -> List

# ALGORITMA 
def DeleteCSVArray (CSVArray : CSVArray, index : int) -> CSVArray :
    
    # membuat CSVArray[index] menjadi None 
    CSVArray.arr = Delete (CSVArray.arr, index)

    # mengurangi jumlah elemen efektif 
    CSVArray.Neff = CSVArray.Neff - 1
    
    return CSVArray

#-----------------------------------------------------------------------------------#

# FUNCTION AMBILBAHAN 
# Function AmbilBahan akan menerima 2 buah CSVArray dan 1 string yang menunjukkan apakah bahan yang diambil adalah untuk bangun/kumpul atau dari database 

# KAMUS LOKAL 
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >

# CSVNama, CSVJumlah : CSVArray
# pasir, batu, air : integer
# argumen : string

# function lcg_rng () -> integer

# ALGORITMA
def AmbilBahan (CSVNama : CSVArray, CSVJumlah : CSVArray, argumen : str) -> (int, int, int) :

    # jika minta bahan random
    if (argumen == "random") : 
        pasir = Lcg_rng()
        batu = Lcg_rng()
        air = Lcg_rng()

    # jika mengecek bahan
    else : # argumen = “data” 
        pasir = int(CSVJumlah.arr[IndexOf(CSVNama.arr, "pasir")])
        batu = int(CSVJumlah.arr[IndexOf(CSVNama.arr, "batu")])
        air = int(CSVJumlah.arr[IndexOf(CSVNama.arr, "air")])

    return (pasir, batu, air)

#-----------------------------------------------------------------------------------#

# FUNCTION SUMCSVARRAY 
# Function CSVArray menerima sebuah CSVArray dan menghitung jumlah total angka dalam array dengan mengubahnya dulu menjadi integer 
#   I.S. sebuah CSVArray
#   F.S. integer 

# KAMUS LOKAL 
# constant Nmax : integer = 103

# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >

# CSVArray : CSVArray
# i, total : integer

# ALGORITMA 
def SumCSVArray ( CSVArray : CSVArray ) -> int :

    # inisialisasi integer 
    total = 0

    # iterasi 
    i = 0

    while (CSVArray.arr[i] != "MARK") :
        if (CSVArray.arr[i] != None) :
            total = total + int(CSVArray.arr[i])
            
        i += 1

    # CSVArray[i] = "MARK"

    return total

#-----------------------------------------------------------------------------------#

# FUNCTION MINCSVARRAY 
# Function MinCSVArray menerima sebuah CSVArray dan mencari nilai terkecil 
#   I.S. 1 buah CSVArray
#   F.S. 2 buah integer yaitu index dengan nilai terkecil dan nilainya 

# KAMUS LOKAL 
# constant Nmax : integer = 103
# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >

# nilaiMin, indexMin : integer
# i : integer

# function int (string : string) -> integer
# { fungsi terdefinisi yang mengubah tipe data string menjadi integer }

# ALGORITMA 
def MinCSVArray (CSVArray : CSVArray) -> (int, int) :

    #inisialisasi variabel 
    nilaiMin = 9999999999999999
    indexMin = 0

    # iterasi 
    i = 0

    while (CSVArray.arr[i] != "MARK") :
        # cek jika ada isinya 
        if (CSVArray.arr[i] != None) :
            if (int(CSVArray.arr[i]) < nilaiMin) :
                nilaiMin = int(CSVArray.arr[i])
                indexMin = i

        i += 1

    # CSVId.arr[i] = “MARK” 

    return (nilaiMin, indexMin)

#-----------------------------------------------------------------------------------#

# FUNCTION MAXCSVARRAY 
# Function MaxCSVArray menerima sebuah CSVArray dan mencari nilai terbesar 
#   I.S. 1 buah CSVArray
#   F.S. 2 buah integer yaitu index dengan nilai terbesar dan nilainya 

# KAMUS LOKAL 
# constant Nmax : integer = 103
# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >

# nilaiMax, indexMax : integer
# i : integer

# function int (string : string) -> integer
# { fungsi terdefinisi yang mengubah tipe data string menjadi integer }

# ALGORITMA 
def MaxCSVArray (CSVArray : CSVArray) -> (int, int) :

    #inisialisasi variabel 
    nilaiMax = 0
    indexMax = 0

    # iterasi 
    i = 0

    while (CSVArray.arr[i] != "MARK") :
        # cek jika ada isinya 
        if (CSVArray.arr[i] != None) :
            if (int(CSVArray.arr[i]) > nilaiMax) :
                nilaiMax = int(CSVArray.arr[i])
                indexMax = i

        i += 1

    # CSVId.arr[i] = “MARK” 

    return (nilaiMax, indexMax)

#-----------------------------------------------------------------------------------#

# FUNCTION TOTALHARGA
# Function TotalHarga mencari total harga pasir, batu, dan air 
#   I.S. 3 buah integer yaitu jumlah pasir, batu, air
#   F.S. sebuah integer yang menjadi total harga 

# KAMUS LOKAL
# pasir, batu, air : integer
# harga : integer

# ALGORITMA 
def TotalHarga (pasir : int, batu : int, air : int) -> int :

    # total
    harga = 10000 * pasir + 15000 * batu + 7500 * air

    return harga
