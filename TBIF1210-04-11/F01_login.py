# import function
from AdditionalFunction import Length, Split, Append
from CSVParser import CSVParser

# FUNGSI LOGIN
# Fungsi Login dibuat untuk mengecek apakah username dan password user terdaftar dalam database atau tidak
# jika terdaftar, user akan masuk sebagai role berdasarkan data, jika tidak terdaftar ataupun password salah
# akan mengembalikan pesan

# KAMUS
#

# ALGORTIMA
def login() :
    
    # mengambil array yang dibutuhkan
    CSVfile = "user.csv"
    CSVUsername = CSVParser(CSVfile, "username")
    CSVPassword = CSVParser(CSVfile, "password")
    CSVRole = CSVParser(CSVfile, "role")
    
    # meminta username dan password
    username = input("Username: ")
    password = input("Password: ")

    # iterasi untuk mengecek username dan password
    i = 0
    while CSVUsername[i] != "MARK" :
        if CSVUsername[i] == username :
            if CSVPassword[i] == password:
                print(f"Selamat datang, {username}!")
                print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")  
                # return role sebagai tanda login
                return CSVRole[i]
            else:
                print("Password salah!")
                break
        else :
            i += 1
    if CSVUsername[i] == "MARK" :
        print("Username tidak terdaftar!")

