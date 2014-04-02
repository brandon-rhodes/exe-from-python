#!/bin/bash

strace -o trace.out "$@"
echo 'open() -' $(grep -cP '^open' trace.out)
echo '  failure -' $(grep -cP '^open.* = -' trace.out)
echo '  success -' $(grep -cP '^open.* = \d' trace.out)
