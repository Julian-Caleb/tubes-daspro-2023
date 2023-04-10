# import function and variable
from AdditionalFunction import Length, Split, Append
from typing import List

# FUNGSI LOGIN
# Fungsi Login dibuat untuk mengecek apakah username dan password user terdaftar dalam database atau tidak
# jika terdaftar, user akan masuk sebagai role berdasarkan data, jika tidak terdaftar ataupun password salah
# akan mengembalikan pesan

# KAMUS
#

# ALGORTIMA
def login(username : str, password : str, role : str, isLoggedIn : bool, CSVUsername: List, CSVPassword: List, CSVRole: List) -> (str, str, str, bool):
    
    # mengecek apakah login atau belum
    # jika sudah
    if isLoggedIn :
        print("Login gagal!")
        print(f'Anda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali. ')
        
    # jika belum    
    else :
       
        # meminta username dan password
        usernameInput = input("Username: ")
        passwordInput = input("Password: ")
        
        # iterasi untuk mengecek username dan password
        i = 0
        while CSVUsername[i] != "MARK" :
            if CSVUsername[i] == usernameInput :
                if CSVPassword[i] == passwordInput:
                    print(f"Selamat datang, {CSVUsername[i]}!")
                    print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')  
                    # return role sebagai tanda login
                    (username, password, role, isLoggedIn) = (CSVUsername[i], CSVPassword[i], CSVRole[i], True)
                    break
                else:
                    print("Password salah!")
                    break
            else :
                i += 1
        if CSVUsername[i] == "MARK" :
            print("Username tidak terdaftar!")
            
    # return username, password, role, isLoggedIn
    return (username, password, role, isLoggedIn)

