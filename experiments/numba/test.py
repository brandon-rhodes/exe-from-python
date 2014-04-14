import numba

#@numba.autojit
@numba.jit('f8,f8')
def f(x, y):
    return x * x + y * y

if __name__ == '__main__':
    print numba.__version__
    f.inspect_types()  # nothing prints
    print f(3, 4)      # prints "25"
    f.inspect_types()
    print f(3.1, 4.1)  # prints "25" (!)
    f.inspect_types()
