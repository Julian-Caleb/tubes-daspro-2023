# FUNCTION LOGOUT 
# Function Logout menerima parameter boolean isLoggedIn, dilakukan pengecekan apakah user sudah login atau belum (memberikan pesan jika belum login), dan mengembalikan string username, password, dan role menjadi string kosong dan isLoggedIn menjadi False (belum login berarti username, password, dan role masih string kosong dan isLoggedIn masih berupa False, yang berarti output baik sudah maupun belum login sama) 
#   I.S. boolean isLoggedIn True atau False
#   F.S. 3 string kosong dan 1 boolean bernilai False 

# KAMUS LOKAL 
# username, password, role : string
# isLoggedIn : boolean

# ALGORTIMA
def Logout(isLoggedIn : bool) -> (str, str, str, bool) :
    
    # Kalau belum login
    if not(isLoggedIn) :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        
    # Jika sudah login, clear username, password, role dan mengubah isLoggedIn menjadi False
    # Jika belum, tidak mengubah apa-apa sehingga username, password, role tetap string kosong dan isLoggedIn tetap False
    return("", "", "", False)
    

        
