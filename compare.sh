#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

for script in $(ls scripts | sed '/\.py$/s/\.py//')
do
    echo ========= $script =========
    echo
    cython/$script
    echo
    nuitka/$script.exe
    echo
    nuitka/$script.dist/$script.exe
    echo
done
