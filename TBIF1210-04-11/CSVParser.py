# Import
from AdditionalFunction import Split, LengthCSV, IndexOf
from typing import List

#  FUNCTION CSVPARSER 
# Function CSVParser berguna untuk membaca sebuah file CSV dan atribut kolom yang diinginkan dan mengembalikan array yang mengandung isi dari atribut kolom parameter 
#   I.S. 2 buah string (1 nama file dan 1 nama kolom yang akan dibuat arraynya)
#   F.S. sebuah array yang berisi konten dari kolom tersebut 

# KAMUS LOKAL 

# constant MARK : string = “MARK”
# constant mark : string = “”
# constant NmaxList : integer = 103
# constant NmaxMatrix : integer = 6

# type List : array [0..NmaxList-1] of string
# array, templateList, arrayColumnName : List

# type MatrixChildren : array [0..NmaxMatrix-1] of string
# templateMatrixChildren : MatrixChildren

# type Matrix : array [0..NmaxList-1] of MatrixChildren
# matrix : Matrix

# file : string
# columnName : string
# indexColumnName : integer
# i : integer

# file : SEQFILE of
# (*) content: string
# (1) mark 

# function LengthCSV (arr : List) -> integer
# function Split (split : string, result : List, splitter : char) -> List
# function IndexOf (arr : List, keyword : string) -> integer

# ALGORITMA
def CSVParser(file : str, columnName : str) -> List : 
    
    # inisiasi variabel mark
    MARK = "MARK"
    
    # mengambil file
    with open(file, 'r') as file:
        data = file.read()
    
    # memetakan data menjadi array dengan menghilangkan newline
    templateList = [None for i in range(104)]
    templateList[0] = MARK
    array = Split(data, templateList, "\n")
    
    # menghilangkan ; dari array, mengubahnya menjadi matrix
    i = 0
    matrix = [None for i in range(104)]
    while (i < LengthCSV(array)) and (array[i] != MARK):
        templateMatrixChildren = [None for i in range (6)]
        templateMatrixChildren[0] = MARK
        matrix[i] = Split(array[i], templateMatrixChildren, ";")
        i += 1
    # (i >= LengthCSV(array)) or (array[i] = "MARK") 
    
    # mencari index atribut column
    indexColumnName = IndexOf(matrix[0], columnName)
    
    # inisialisasi array baru dengan Mark
    arrayColumnName = [None for i in range (103)]
    arrayColumnName[0] = MARK
    
    # memasukkan isi dari kolom ke dalam array baru (arrayColumnName)
    i = 1
    while array[i] != MARK :
        if array[i] != [''] :
            arrayColumnName[i], arrayColumnName[i-1] = MARK, matrix[i][indexColumnName]
            i += 1
        else :
            break
    
    return arrayColumnName

# APLIKASI
# test = "save/18-04-2023/candi.csv"
# print(CSVParser(test, "id"))

#-----------------------------------------------------------------------------------#