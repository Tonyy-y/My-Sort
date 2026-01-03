#!/bin/bash
dos2unix main.sh generateArray.sh bitonicSort.sh shellSort.sh
./generateArray.sh numbers.in 1024 random 
printf "\nRuntime for Shell Sort:"
time ./shellSort.sh numbers.in numbers.out desc
printf "\nRuntime for Bitonic Sort:"
time ./bitonicSort.sh numbers.in numbers.out desc
printf "\nRuntime for sort -n:"
time sort -n -r numbers.in > numbers.out
