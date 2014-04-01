# DOCKER-VERSION 0.9.1

FROM ubuntu:13.10
RUN apt-get -y install libpython2.7
ADD cython cython
ADD nuitka nuitka
ADD scripts scripts
ADD compare.sh compare.sh
