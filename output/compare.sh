#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

for script in $(ls cython)
do
    echo "======================================== Cython: $script"
    ./cython/$script
    echo "======================================== Nuitka: $script"
    ./nuitka/$script.dist/$script.exe
    echo
done
