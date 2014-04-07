
# gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
#       -I/usr/include/python2.5 -o yourmod.so yourmod.c

something: example_python2.py
	python3.4 setup.py build_ext --inplace

#example_python2.c: example_python2.py
#	cython $<

run:
	python3.4 -c 'import example_python2; example_python2.two()'

clean:
	rm -f *.c *.so
