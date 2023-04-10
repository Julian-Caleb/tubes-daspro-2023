# Import
from typing import List

# FUNCTION LENGTH
# Fungsi dibuat untuk menentukan banyak elemen dalam suatu array

# KAMUS
# arr : array of elements (integer atau char)

# ALGORITMA
def Length (arr : List) -> List :
    return len(arr)


def Length2 (arr : List) -> List :
    count = 0
    for i in arr:
        count+=1
    return count
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
#

# KAMUS 
#

# ALGORITMA
def Append (arr : List, element : str) -> List :
    return arr.append(element) # sementara

def Append2 (a, n) :
    z = a + n
    return z # sama gk nih? element nya tuh list bukan?

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