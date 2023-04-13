# Import
from AdditionalFunction import Split, Length
from typing import List

# FUNCTION INDEXCOLUMNNAME
# Fungsi IndexColumnName menerima sebuah array dan string mencari pada index ke berapa string itu terdapat

# KAMUS
# 

# ALGORITMA
def IndexColumnName (arr : List, X : str) :
    # Asumsikan pasti ketemu
    
    # inisialisasi index string yang dicari
    i = 0
    while i < Length(arr) and arr[i] != X :
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
    
    # mengambil file
    with open(file, 'r') as file:
        data = file.read()
    
    # memetakan data menjadi array
    array = Split(data, "\n")
    
    # menghilangkan ; dari array, mengubahnya menjadi matrix
    i = 0
    while i < Length(array) :
        array[i] = Split(array[i], ";")
        i += 1
        
    # mencari index atribut column
    indexColumnName = IndexColumnName(array[0], columnName)
    
    # Inisialisasi array baru dengan Mark
    arrayColumnName = [None for i in range (103)]
    MARK = "MARK"
    arrayColumnName[0] = MARK
    
    # Memasukkan isi dari kolom ke dalam array baru (arrayColumnName)
    i = 1
    while i < Length(array) - 1 :
        arrayColumnName[i], arrayColumnName[i-1] = MARK, array[i][indexColumnName]
        i += 1
    
    return arrayColumnName

# APLIKASI
# print(CSVParser("user.csv", "role"))

#-----------------------------------------------------------------------------------#

