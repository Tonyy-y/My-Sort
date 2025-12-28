#!/bin/bash
readarray -t arr < numbers.in
n=${#arr[@]}
for ((gap=n>>1; gap>=1; gap>>=1)); do
    for ((i=gap; i<n; i++)); do
        x=${arr[$i]}
        j=$i
        while ((j>=gap && arr[j-gap]>x)); do
            arr[$j]=${arr[$j-$gap]}
            ((j-=gap))
        done
        arr[$j]=$x
    done
done
printf "%d\n" ${arr[@]} > numbers.out
