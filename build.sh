#!/bin/bash

set -e
cd $(dirname "${BASH_SOURCE[0]}")

rm -rf output/cython output/nuitka pyinstaller/dist
mkdir -p output/cython output/nuitka pyinstaller

if [ "$#" = "1" -a "$1" = "all" ]
then
    scripts="cascade harmonic_sum hello needs_crypto needs_flask needs_m2crypto"
elif [ "$#" = "0" ]
then
    scripts="hello"
else
    scripts="$@"
fi

for script in $scripts
do
    (cd cython && make TARGET=$script)
    cp cython/$script output/cython/$script
    (cd nuitka && make TARGET=$script)
    cp -r nuitka/$script.dist output/nuitka/
    #(cd pyinstaller && pyinstaller --onefile ../scripts/$script.py)
done
