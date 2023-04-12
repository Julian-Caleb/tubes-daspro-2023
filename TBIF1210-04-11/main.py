# PROGRAM UTAMA
# 

# KAMUS GLOBAL
# constant NMax = 100

# username : string 
# password : string
# role : string
# func : string 
# isLoggedIn : boolean

# CSVfile : string
# type CSVArray : <arr : array [0..NMax-1] of string,
# 				Neff : integer >
# CSVUsername : CSVArray
# CSVPassword : CSVArray
# CSVRole : CSVArray

# ALGORITMA
# import function
from CSVParser import CSVParser
from AdditionalFunction import Length, LengthArray
from TipeBentukan import CSVArray
from F01_login import Login
from F02_logout import Logout

# main program
# inisialisasi variable
(username, password, role, isLoggedIn) = ("", "", "", False)
seed = 69 # sebagai seed untuk algoritma lcg_rng

# mengambil array yang dibutuhkan
CSVfile = "user.csv"
CSVUsername = CSVArray(CSVParser(CSVfile, "username"), LengthArray(CSVParser(CSVfile, "username")))
CSVPassword = CSVArray(CSVParser(CSVfile, "password"), LengthArray(CSVParser(CSVfile, "password")))
CSVRole = CSVArray(CSVParser(CSVfile, "role"), LengthArray(CSVParser(CSVfile, "role")))

# looping 
while True :
    func = input(">>> ")
    
    # F01 - login
    if func == "login" :
        (username, password, role, isLoggedIn) = Login(username, password, role, isLoggedIn, CSVUsername, CSVPassword, CSVRole)
        # print (username, password, role, isLoggedIn)
        
    # F02 - logout
    elif func == "logout" :
        (username, password, role, isLoggedIn) = Logout(isLoggedIn)
        # print (username, password, role, isLoggedIn)
        
    # print(username)

