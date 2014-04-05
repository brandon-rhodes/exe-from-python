from numba import export

def mult(a, b):
    return a * b

export('mult f8(f8, f8)')(mult)
