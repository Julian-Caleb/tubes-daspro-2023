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
    
    # F01 - login
    if func == "login" :
        role = login()
        # print(role)
        
    # F02 - logout
    elif func == "logout" :
        role = logout()


