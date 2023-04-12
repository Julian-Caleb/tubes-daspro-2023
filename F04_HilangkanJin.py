def HapusJin (role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir):
    
    # Mengecek apakah (role) diisi dengan "bandung_bondowoso"
    # Jika tidak
    if role != "bandung_bondowoso":
        return [role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir]
    
    # Jika ya, input nama jin ke dalam (usernameJin)
    else:
        usernameJin = str(input("Masukkan username jin : "))
    
        # Jika (usernameJin) tidak terdaftar pada (CSVUsername)
        if usernameJin not in CSVUsername:
            print("Tidak ada jin dengan username tersebut.")
            
        # Jika (usernameJin) terdaftar pada (CSVUsername)
        else:
            
            # Mengganti semua data jin tersebut yang ada pada beberapa list dengan None
            for i in range(len(CSVUsername)):
                 if CSVUsername[i] == usernameJin:
                    CSVUsername[i] = None
                    CSVPassword[i] = None
                    CSVRole[i] = None
                    CSVId[i] = None
                    CSVPembuat[i] = None
                    CSVPasir[i] = None
                    CSVBatu[i] = None
                    CSVAir[i] = None
                    
        return [role, CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir]