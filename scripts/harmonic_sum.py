import sys
from time import time

ten_million = 10000000
xrange = range if sys.version_info >= (3, 0) else xrange

def compute_harmonic_sum(terms=ten_million):
    t0 = time()
    n = 0.0
    for i in xrange(1, terms + 1):
        n += 1.0 / i
    t1 = time()
    print('Sum {}'.format(n))
    print('Milliseconds {}'.format((t1 - t0) * 1000.0))

def compute_harmonic_sum_with_numpy(terms=ten_million):
    import numpy as np
    t0 = time()
    v = np.arange(1.0, terms + 1.0, 1.0)
    n = (1.0 / v).sum()
    t1 = time()
    print('Sum {}'.format(n))
    print('Milliseconds {}'.format((t1 - t0) * 1000.0))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        compute_harmonic_sum_with_numpy(terms=ten_million)
    else:
        compute_harmonic_sum()
