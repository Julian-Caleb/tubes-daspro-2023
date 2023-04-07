from AdditionalFunction import Length, Split, Append

# FUNGSI LOGIN
# 

# KAMUS
#

# ALGORTIMA
def login() :
    
    # mengambil file
    with open('user.csv', 'r') as file:
        data = file.read()
        
    # memetakan data menjadi array
    arrayOfData = Split(data, "\n")
    
    # menghilangkan ; dari array
    i = 0
    while i < Length(arrayOfData) :
        arrayOfData[i] = Split(arrayOfData[i], ";")
        i += 1
    
    # meminta username dan password
    username = input("Username: ")
    password = input("Password: ")

    # iterasi untuk mengecek username dan password
    i = 0
    while i < Length(arrayOfData) :
        if arrayOfData[i][0] == username :
            if arrayOfData[i][1] == password:
                print(f"Selamat datang, {username}!")
                print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                
                # return role sebagai tanda login
                return(arrayOfData[i][2])
            else:
                print("Password salah!")
                break
        elif i == Length(arrayOfData) - 1:
            print("Username tidak terdaftar!")
            break
        else :
            i += 1
    
    
    

            

