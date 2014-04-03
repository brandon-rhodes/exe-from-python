#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

for script in $(ls cython)
do
    echo ========= $script =========
    echo
    ./cython/$script
    echo
    ./nuitka/$script.dist/$script.exe
    echo
done
