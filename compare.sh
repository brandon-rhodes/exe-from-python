#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

for script in $(ls scripts | sed '/\.py$/s/\.py//')
do
    echo ========= $script =========
    echo
    cython/$script
    echo
    if [ -x nuitka/$script.exe ]
    then
        nuitka/$script.exe
    else
        nuitka/$script.dist/$script.exe
    fi
    echo
done
