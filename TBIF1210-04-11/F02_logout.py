# FUNGSI LOGOUT
# 

# KAMUS
#

# ALGORTIMA
def Logout(isLoggedIn : bool) -> (str, str, str, bool) :
    
    # Kalau belum login
    if not(isLoggedIn) :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        
    # Jika sudah login, clear username, password, role dan mengubah isLoggedIn menjadi False
    # Jika belum, tidak mengubah apa-apa sehingga username, password, role tetap string kosong dan isLoggedIn tetap False
    return("", "", "", False)
    

        
