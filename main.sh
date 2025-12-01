#!/bin/bash
printf "Runtime for Shell Sort:"
time ./shellSort.sh
printf "\nRuntime for Bitonic Sort:"
time ./bitonicSort.sh
printf "\nRuntime for sort -n:"
time sort -n numbers.in > numbers.out
