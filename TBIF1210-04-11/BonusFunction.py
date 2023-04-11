# FUNCTION LCG_RNG
# 

# KAMUS
#

# ALGORITMA
def lcg_rng(seed : int, a : int = 1103515245, c : int = 12345, m : int = 2**31):
    seed = (a * seed + c) % m
    rand = seed % 5 + 1
    return rand

# APLIKASI 
# rand = lcg_rng(seed = 1001234121501)
# print(rand)

