#!/bin/bash

set -e
cd $(dirname "${BASH_SOURCE[0]}")

V2=~/.v/exe-from-python
V3=~/.v/exe-from-python-experiments-py23

if [ ! -f boto-2.27.0.tar.gz ]
then
    wget https://pypi.python.org/packages/source/b/boto/boto-2.27.0.tar.gz
fi

rm -rf boto-2.27.0/ boto/ build/
tar xfz boto-2.27.0.tar.gz boto-2.27.0/boto
cp -r boto-2.27.0/boto/ .

sed -i 's/sys.stdout/None/' boto/requestlog.py

#python2.7 setup.py build_ext --inplace
#python3.4 setup.py build_ext --inplace

for source in \
    boto/[a-z]*.py \
    boto/gs/[a-z]*.py \
    boto/pyami/[a-z]*.py \
    boto/s3/[a-z]*.py
do
    base=${source%.py}
    $V2/bin/cython --lenient $base.py
    gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
        -I$V3/include/python3.4m -o $base.so $base.c
    #exit
done

mv boto/__init__.py .
cat preamble.py __init__.py > boto/__init__.py
rm __init__.py

find boto -name '[a-z]*.py' | xargs rm
