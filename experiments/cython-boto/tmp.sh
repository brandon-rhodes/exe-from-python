
set -e
set -v

V3=~/.v/exe-from-python-experiments-py23

echo $V3/include/python3.4

gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
    -I$V3/include/python3.4m -o boto/auth.so boto/auth.c
