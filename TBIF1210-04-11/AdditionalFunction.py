# Import
from typing import List
from TipeBentukan import CSVArray

#-----------------------------------------------------------------------------------#
# FUNCTION LENGTHARRAY 
# Fungsi LengthArray menerima sebuah array dan mengembalikan banyak elemen efektif dari indeks 0 hingga elemen sebelum MARK 
#   I.S. Sebuah array yang mengandung MARK
#   F.S. Banyak elemen efektif 

# KAMUS LOKAL 
# constant Nmax : int = 103
# type arr: array [0..Nmax-1] of str
# i, count : int

# ALGORITMA 
def LengthArray (arr: List) -> int :
    
    # inisialisasi variabel
    i = 0
    count = 0
    
    # mengecek mark
    while (arr[i] != 'MARK') :
        
        # apabila elemen tidak kosong
        if (arr[i] != None) :
        
            # menambahkan jumlah elemen
            count += 1
        
        i += 1
            
    return i

# APLIKASI
# print(LengthArray(['Bondowoso', 'Roro', 'Lmao', 'MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]))

#-----------------------------------------------------------------------------------#

# FUNCTION LENGTH
# Fungsi dibuat untuk menentukan banyak elemen efektif dalam suatu array

# KAMUS
# arr : array of elements (integer atau char)

# ALGORITMA
def Length (arr : List) -> int : # pengganti len()
    # Menggunakan "MARK" sebagai mark
    # i = 0
    # while arr[i] != "MARK" :
    #     i += 1
    # return i
    return len(arr)

def Length2 (arr):
    x = list(arr) + ['']
    i = 0
    while x[i] != '':
        i+=1
    return i
    
# APLIKASI
# print(Length(["a", "b", "c", "d", "MARK", None]))

#-----------------------------------------------------------------------------------#

# FUNCTION SPLIT
#

# KAMUS 
#

# ALGORITMA
def Split (arr : List, spliter : str) -> List :
    return arr.split(spliter) # sementara

#-----------------------------------------------------------------------------------#

# FUNCTION APPEND 
# Fungsi Append menerima sebuah array dan string, menambahkan string pada array dan menambahkan 1 pada array.
#   I.S.
#   F.S. 

# KAMUS LOKAL 

# constant Nmax : integer = 103
# arr : array [0..Nmax-1] of string
# i : integer

# ALGORITMA
def Append (arr : List, element : str) -> List :

    # inisialisasi variabel 
    i <- 0

    # elemen akan dimasukkan pada elemen yang kosong pada array (None) atau di paling belakang (menggeser array) dengan asumsi pasti ada “MARK” 

    # iterasi hingga menemukan None atau “MARK” dengan skema search
    while (arr[i] != None) or (arr[i] != "MARK") :
        i <- i + 1 

    # memasukkan dan menggeser
    if (arr[i] == None) :
        arr[i] = element
    else : # arr[i] = “MARK” 
        arr[i] = element
        arr[i+1] = "MARK"
    return arr

#-----------------------------------------------------------------------------------#

def Append2 (a, n) :
    z = a + n
    return z # sama gk nih? element nya tuh list bukan?

#-----------------------------------------------------------------------------------#

# FUNCTION APPENDCSVARRAY 
# Fungsi AppendCSVArray menerima sebuah CSVarray dan string, menambahkan string pada CSVarray.arr dan menambahkan 1 pada CSVArray.Neff.
#   I.S. 
#   F.S. 

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
    CSVArray.Neff <- CSVArray.Neff + 1

    return arr

#-----------------------------------------------------------------------------------#

# FUNCTION ORDCHAR
#

# KAMUS 
#

# ALGORITMA
def OrdChar (x : str) -> int :
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    index = 0 
    while x != alphabet[index] :
        index += 1
    return index

#-----------------------------------------------------------------------------------#

# FUNCTION COMPARESTRING
# Function CompareString dibuat untuk menerima input 2 string dan operator (> atau <).
# membandingkan leksikografis antara 2 string, mengembalikan string
# dengan leksikografis lebih tinggi atau rendah berdasarkan operatornya

# KAMUS 
#

# ALGORITMA
def CompareString (stringOne : str, stringTwo : str, op : str) -> str : 
    # asumsi perbandingan hanya lebih besar atau lebih kecil
    
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
# Function CompareArrayOfString menerima array of string dan operator dan mengembalikan string dengan
# leksikografis tertinggi / terendah berdasarkan operatornya

# KAMUS
# 

# ALGORITMA
def CompareArrayOfString (arr : List, op : str) -> List :
    output = arr[0]
    n = 1
    while n < Length(arr) :
        output = CompareString (output, arr[n], op)
        n += 1
        
    return output

#-----------------------------------------------------------------------------------#

# FUNCTION INDEXOF 
# function IndexOf menerima input sebuah array of string dan sebuah keyword string, mencari pada index keberapa string tersebut berada pada array (membaca index pertama kali string tersebut muncul) dan mengembalikan index tersebut. Asumsi string pasti ditemukan (dikarenakan pemanggilan MemberOf sebelum IndexOf).
#	I.S. sebuah array of string dan sebuah string
#	F.S. integer index keberapa string tersebut (pertama kali) muncul pada array 

# KAMUS LOKAL 
# constant NMax : int = 103
# arr : array [0..Nmax-1] of str
# keyword : str
# i : int

# ALGORITMA
def IndexOf (arr : List, keyword : str) -> int :

    # inisialisasi iterasi 
    i = 0
		
	# iterasi dilakukan hingga keyword ditemukan 
    while (arr[i] != keyword) :
        i += 1
        
    # arr[i] = keyword 
    IX = i + 1
    return i

# APLIKASI
# print(IndexOf(["a","b","c","d","e"], "d"))

#-----------------------------------------------------------------------------------#

# FUNCTION MEMBEROF 
# function MemberOf menerima input sebuah array of string dan sebuah keyword string, mencari apakah string keyword berada pada array dan mengembalikan boolean, True jika ada dan False jika tidak. 
#	I.S. sebuah array of string dan sebuah string
#	F.S. boolean, True jika ditemukan, False jika tidak.

# KAMUS LOKAL 
# constant NMax : int = 103
# arr : array [0..Nmax-1] of str
# keyword : str
# Found : bool
# i : int 

# ALGORITMA 
def MemberOf (arr: List, keyword : str) -> bool :
    
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
#   I.S. sebuah array of string dan sebuah string 
#   F.S. integer banyak kemunculan string tersebut dalam array 

# KAMUS LOKAL 
# constant Nmax : int = 103
# arr : array [0..Nmax-1] of str
# keyword : str
# i, count : int

# ALGORITMA 
def Frequency (arr : List, keyword : str) -> int :
    
    # inisialisasi iterasi
    Nmax = 103
    i = 0
    count = 0
    
    # iterasi menghitung berapa kali ditemukan
    while (i < Nmax) :
        if (arr[i] == keyword) :
            count += 1
        i += 1
    
    return count

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
# type arr : array [0..Nmax-1] of str

# ALGORITMA
def Delete (arr : List, index : int) -> List :
    
    # membuat arr[index] menjadi None
    arr[index] = None
    
    return arr

# APLIKASI
# print(Delete(['bandung_bondowoso', 'roro_jonggrang', 'MARK', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
#                  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 1))

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


