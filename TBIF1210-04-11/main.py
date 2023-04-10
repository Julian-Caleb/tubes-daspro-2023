# PROGRAM UTAMA
# 

# KAMUS GLOBAL
# 

# ALGORITMA
# import function
from CSVParser import CSVParser
from F01_login import login
from F02_logout import logout

# main program
# inisialisasi variable
(username, password, role, isLoggedIn) = ("", "", "", False)

# mengambil array yang dibutuhkan
CSVfile = "user.csv"
CSVUsername = CSVParser(CSVfile, "username")
CSVPassword = CSVParser(CSVfile, "password")
CSVRole = CSVParser(CSVfile, "role")

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

