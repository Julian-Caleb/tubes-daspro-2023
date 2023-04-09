# FUNCTION LCG_RNG
# 

# KAMUS
#

# ALGORITMA
def lcg_rng(seed : int, a : int = 1103515245, c : int = 12345, m : int = 2**31):
    while True:
        seed = (a * seed + c) % m
        rand = seed / m
        return rand

# APLIKASI 
rand = lcg_rng(seed=123)
print(rand)

