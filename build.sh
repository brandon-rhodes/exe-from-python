#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

mkdir -p output/cython output/nuitka

for script in $(ls scripts | sed '/\.py$/s/\.py//')
do
    (cd cython && make TARGET=$script)
    cp cython/$script output/cython/$script
    (cd nuitka && make TARGET=$script)
    cp nuitka/$script.dist/$script.exe output/nuitka/$script
done
