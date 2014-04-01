#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

for script in $(ls scripts | sed '/\.py$/s/\.py//')
do
    (cd cython && make TARGET=$script)
    (cd nuitka && make TARGET=$script)
done
