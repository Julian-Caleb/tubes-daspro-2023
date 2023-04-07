# PROGRAM UTAMA
# 

# KAMUS GLOBAL
# 

# ALGORITMA
# import function
from F01_login import login
from F02_logout import logout

# main program
while True :
    func = input(">>> ")
    if func == "login" :
        role = login()
    elif func == "logout" :
        role = logout()


