import numba
import timeit

def h(start, terms):
    n = start
    for i in xrange(1, terms):
        n += 1.0 / i
    return n

def call_h():
    h(0.0, 10000000)

h2 = numba.jit(h)

def call_h2():
    h2(0.0, 10000000)

h3 = numba.jit('f8,int64')(h)

def call_h3():
    h3(0.0, 10000000)

if __name__ == '__main__':
    #print harmonic_sum()
    #print timeit(harmonic_sum, number=1)
    print min(timeit.repeat(call_h2, number=1))
    print min(timeit.repeat(call_h3, number=1))
