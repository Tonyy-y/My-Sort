#!/bin/bash
input_file=$1
output_file=$2
order=$3
readarray -t arr < $input_file
n=${#arr[@]}
[[ $order == "desc" ]] && comp=0 || comp=1
gaps=(301 132 57 23 10 4 1)
h=701
while ((h<n)); do
    gaps=($h "${gaps[@]}")
    h=$(((h * 225) / 100))
    ((h%2 == 0)) && ((h++))
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
