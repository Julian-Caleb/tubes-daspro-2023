# FUNCTION LCG_RNG
# 

# KAMUS
#

# ALGORITMA
def lcg_rng(seed, a=1103515245, c=12345, m=2**31):
    while True:
        seed = (a * seed + c) % m
        rand = seed / m
        return rand
rand = lcg(seed=123)
print(rand)