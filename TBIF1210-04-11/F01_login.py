# import library
import csv
import os

# fungsi login
def login() :
    
    # mengambil file
    with open("user.csv") as file:
        reader = csv.reader(file)
        
        # mencetak isi
        for row in reader :
            print(row)