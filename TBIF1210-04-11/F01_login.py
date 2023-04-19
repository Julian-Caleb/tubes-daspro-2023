# import function and variable
from AdditionalFunction import Split, Append
from TipeBentukan import CSVArray
from typing import List

# FUNCTION LOGIN 
# Function Login meminta username dan password dari user dan mengembalikan output berdasarkan terdaftar tidaknya atau benar salahnya username dan password yang diinput user berdasarkan database CSVArray yang ada. 
#   I.S. 3 buah string (username, password, dan role), 1 buah boolean (isLoggedIn), dan 3 buah CSVArray (CSVUsername, CSVPassword, CSVRole) 
#   F.S. mengembalikan string username, password, dan role yang kosong jika tidak terdaftar atau terisi (sesuai dengan input dan data base) jika terdaftar dan boolean isLoggedIn menjadi True jika terdaftar atau False jika tidak terdaftar. 

# KAMUS LOKAL 
# constant Nmax : integer = 103

# username, usernameInput : string 
# password, passwordInput : string
# role : string
# isLoggedIn, stopChecking : boolean
# 	i : integer

# CSVfile : string
# type CSVArray : <arr : array [0..Nmax-1] of string,
# 				Neff : integer >
# CSVUsername, CSVPassword, CSVRole : CSVArray

# ALGORTIMA
def Login(username : str, password : str, role : str, isLoggedIn : bool, CSVUsername: CSVArray, CSVPassword: CSVArray, CSVRole: CSVArray) -> (str, str, str, bool):
    
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
        while CSVUsername.arr[i] != "MARK" :
            if CSVUsername.arr[i] == usernameInput :
                if CSVPassword.arr[i] == passwordInput:
                    print(f"Selamat datang, {CSVUsername.arr[i]}!")
                    print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')  
                    # return role sebagai tanda login
                    (username, password, role, isLoggedIn) = (CSVUsername.arr[i], CSVPassword.arr[i], CSVRole.arr[i], True)
                    break
                else:
                    print("Password salah!")
                    break
            else :
                i += 1
        if CSVUsername.arr[i] == "MARK" :
            print("Username tidak terdaftar!")
            
    # return username, password, role, isLoggedIn
    return (username, password, role, isLoggedIn)

