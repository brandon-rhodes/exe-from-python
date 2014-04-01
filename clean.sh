#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")
rm -f cython/*.c cython/*.o nuitka/*.exe
rm -rf nuitka/*.build
