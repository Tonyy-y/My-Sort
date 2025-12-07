#!/bin/bash

shellSort() {
    declare -n arr=$1
    local n=${#arr[@]}
    for ((gap=n>>1; gap>=1; gap>>=1)); do
        for ((i=gap; i<n; i++)); do
            local x=${arr[$i]}
            local j=$i
            while ((j>=gap && arr[j-gap]>x)); do
                arr[$j]=${arr[$j-$gap]}
                ((j-=gap))
            done
            arr[$j]=$x
        done
    done
}

readarray -t v < numbers.in
shellSort v
printf "%d\n" ${v[@]} > numbers.out
