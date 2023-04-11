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
from AdditionalFunction import Length
from TipeBentukan import CSVArray
from F01_login import login
from F02_logout import logout

# main program
# inisialisasi variable
(username, password, role, isLoggedIn) = ("", "", "", False)

# mengambil array yang dibutuhkan
CSVfile = "user.csv"
CSVUsername = CSVArray(CSVParser(CSVfile, "username"), Length(CSVParser(CSVfile, "username")))
CSVPassword = CSVArray(CSVParser(CSVfile, "password"), Length(CSVParser(CSVfile, "password")))
CSVRole = CSVArray(CSVParser(CSVfile, "role"), Length(CSVParser(CSVfile, "role")))

# looping 
while True :
    func = input(">>> ")
    
    # F01 - login
    if func == "login" :
        (username, password, role, isLoggedIn) = login(username, password, role, isLoggedIn, CSVUsername, CSVPassword, CSVRole)
        # print (username, password, role, isLoggedIn)
        
    # F02 - logout
    elif func == "logout" :
        (username, password, role, isLoggedIn) = logout(isLoggedIn)
        # print (username, password, role, isLoggedIn)
        
    # print(username)

