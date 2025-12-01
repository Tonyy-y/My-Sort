#!/bin/bash
readarray -t v < numbers.in
n=${#v[@]}
for ((gap=n>>1; gap>=1; gap>>=1)); do
    for ((i=gap; i<n; i++)); do
        x=${v[$i]}
        j=$i
        while ((j>=gap && v[j-gap]>x)); do
            v[$j]=${v[$j-$gap]}
            ((j-=gap))
        done
        v[$j]=$x
    done
done
printf "%d\n" ${v[@]} > numbers.out
