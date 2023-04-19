# Import
from AdditionalFunction import Split, LengthCSV
from typing import List

# FUNCTION INDEXCOLUMNNAME
# Fungsi IndexColumnName menerima sebuah array dan string mencari pada index ke berapa string itu terdapat

# KAMUS
# arr : array of string
# x : string

# i : integer

# function LengthCSV (arr : arr) -> integer

# ALGORITMA
def IndexColumnName (arr : List, X : str) :
    # Asumsikan pasti ditemukan
    
    # inisialisasi index string yang dicari
    i = 0
    while i < LengthCSV(arr) and arr[i] != X :
        i += 1
    
    return i

#-----------------------------------------------------------------------------------#

# FUNCTION CSVPARSER
# Fungsi CSVParser berguna untuk membaca sebuah file CSV dan atribut kolom yang diinginkan dan mengembalikan array yang mengandung
# isi dari atribut kolom parameter

# KAMUS
# 

# ALGORITMA
def CSVParser(file : str, columnName : str) -> List : 
    
    # inisiasi variabel mark
    MARK = "MARK"
    
    # mengambil file
    with open(file, 'r') as file:
        data = file.read()
    
    # memetakan data menjadi array
    result = [None for i in range(103)]
    result[0] = "MARK"
    array = Split(data, result, "\n")
    
    # # menghilangkan ; dari array, mengubahnya menjadi matrix
    i = 0
    while i < LengthCSV(array) and array[i] != "MARK":
        result = [None for i in range (6)]
        result[0] = "MARK"
        array[i] = Split(array[i], result, ";")
        i += 1
    
    # mencari index atribut column
    indexColumnName = IndexColumnName(array[0], columnName)
    
    # Inisialisasi array baru dengan Mark
    arrayColumnName = [None for i in range (103)]
    arrayColumnName[0] = MARK
    
    # Memasukkan isi dari kolom ke dalam array baru (arrayColumnName)
    i = 1
    while array[i] != MARK :
        if array[i] != [''] :
            arrayColumnName[i], arrayColumnName[i-1] = MARK, array[i][indexColumnName]
            i += 1
        else :
            break
    
    return arrayColumnName

# APLIKASI
# test = "default/user.csv"
# print(CSVParser(test, "username"))

#-----------------------------------------------------------------------------------#