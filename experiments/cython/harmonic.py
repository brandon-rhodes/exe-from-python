import timeit

def h(start, terms):
    n = start
    for i in xrange(1, terms):
        n += 1.0 / i
    return n

def call_h():
    return h(0.0, 10000000)

if __name__ == '__main__':
    print call_h()
    print min(timeit.repeat(call_h, number=1))
