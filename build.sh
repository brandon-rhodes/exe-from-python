#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

rm -rf output/cython output/nuitka pyinstaller/dist
mkdir -p output/cython output/nuitka pyinstaller

for script in $(ls scripts | sed '/\.py$/s/\.py//')
do
    (cd cython && make TARGET=$script)
    cp cython/$script output/cython/$script
    (cd nuitka && make TARGET=$script)
    cp -r nuitka/$script.dist output/nuitka/
    (cd pyinstaller && pyinstaller --onefile ../scripts/$script.py)
done
