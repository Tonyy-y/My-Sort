#!/bin/bash
input_file=$1
output_file=$2
order=$3
readarray -t arr < $input_file
n=${#arr[@]}
[[ $order == "desc" ]] && comp=0 || comp=1
gaps=()
h=1
while ((h < n/3)); do
    gaps=($h "${gaps[@]}")
    h=$((3 * h + 1))
done
for gap in "${gaps[@]}"; do
    for ((i=gap; i<n; i++)); do
        x=${arr[$i]}
        j=$i
        while ((j>=gap && arr[j-gap]>x == comp)); do
            arr[$j]=${arr[$j-$gap]}
            ((j-=gap))
        done
        arr[$j]=$x
    done
done
printf "%d\n" ${arr[@]} > $output_file
