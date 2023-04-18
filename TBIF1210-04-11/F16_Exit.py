from F14_Save import Save
from TipeBentukan import CSVArray

# PROCEDURE EXIT
# Procedure Exit bertujuan untuk user dapat melakukan penyimpanan (jika ingin dilakukan) dan keluar dari program
# I.S. -
# F.S. Keluar program

# KAMUS LOKAL
# response : char

# function exit() { fungsi bawaan python untuk keluar dari program }
# procedure Save

def Exit(CSVUsername : CSVArray, CSVPassword : CSVArray, CSVRole : CSVArray, CSVId : CSVArray, CSVPembuat : CSVArray, CSVPasir : CSVArray, CSVBatu : CSVArray, CSVAir : CSVArray, CSVNama : CSVArray, CSVDeskripsi : CSVArray, CSVJumlah : CSVArray):
    # Iterasi hingga ditemukan respon yang benar
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end =" ")
    response = str(input())
    while response != "Y" and response != "y" and response != "N" and response != "n":
        response = str(input())
    # Jika ingin disimpan
    if response == "Y" or response == "y":
        Save(CSVUsername, CSVPassword, CSVRole, CSVId, CSVPembuat, CSVPasir, CSVBatu, CSVAir, CSVNama, CSVDeskripsi, CSVJumlah)
    # Keluar program
    exit()