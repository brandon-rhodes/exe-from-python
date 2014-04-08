import numba
import timeit

def h(start, terms):
    n = start
    for i in xrange(1, terms):
        n += 1.0 / i
    return n

def call_h():
    return h(0.0, 10000000)

def h2(start, terms):
    cdef double n = start
    cdef int i
    for i in xrange(1, terms):
        n += 1.0 / i
    return n

def call_h2():
    return h2(0.0, 10000000)

def main():
    print call_h()
    print call_h2()
    print min(timeit.repeat(call_h, number=1))
    print min(timeit.repeat(call_h2, number=1))

if __name__ == '__main__':
    main()
