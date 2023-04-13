import time

# FUNCTION LCG_RNG
# 

# KAMUS LOKAL
# seed : int
# a : int = 1103515245
# c : int = 12345
# m : int = 2**31

# ALGORITMA
def Lcg_rng():
    time.sleep(0.001) # delay
    seed = int(round(time.time() * 1000))
    a = 1103515245
    c = 12345
    m = 2**31
    
    seed = seed % m
    seed = (a * seed + c) % m
    rand = seed % 5 + 1
    return (int(rand))

# APLIKASI 
pasir = Lcg_rng()
batu = Lcg_rng()
air = Lcg_rng()

print(pasir, batu, air)


