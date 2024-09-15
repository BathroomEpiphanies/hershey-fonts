#!/usr/bin/bash

rm -rf 'build'
mkdir -p 'build'

sed 's|// #define|#define|' 'libhersheyfont/hersheyfont.c' > 'build/hersheyfont.c'
cat 'libhersheyfont/hersheyfont.h' > 'build/hersheyfont.h'
sed 's|#include <hersheyfont.h>|#include "hersheyfont.h"|' 'tools/hershey-font-gnuplot.c' > 'build/hershey-font-gnuplot.c'

pushd 'build'
gcc -Wall 'hersheyfont.c' 'hershey-font-gnuplot.c' -l 'unistring' -o 'hershey-font-gnuplot'
popd
