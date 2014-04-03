#!/bin/bash

set -e
cd $(dirname "${BASH_SOURCE[0]}")
cd output
docker build -t exe/test .
exec docker run exe/test ./compare.sh
