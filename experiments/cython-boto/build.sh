#!/bin/bash

set -e
cd $(dirname "${BASH_SOURCE[0]}")

if [ ! -f boto-2.27.0.tar.gz ]
then
    wget https://pypi.python.org/packages/source/b/boto/boto-2.27.0.tar.gz
fi

rm -rf boto-2.27.0/ boto/ build/
tar xfz boto-2.27.0.tar.gz boto-2.27.0/boto
cp -r boto-2.27.0/boto/ .

sed -i 's/sys.stdout/None/' boto/requestlog.py

python setup.py build_ext --inplace

find boto -name '[a-z]*.py' | xargs rm
