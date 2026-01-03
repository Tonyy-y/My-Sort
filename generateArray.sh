#!/bin/bash
file=$1
size=$2
type=$3
printf "" > $file
case $type in
    "desc")
        for ((i=size; i>=1; i--)); do
            printf "%d\n" $i >> $file
        done
        ;;
    "random")
        for ((i=1; i<=size; i++)); do
            printf "%d\n" $RANDOM >> $file
        done
        ;;
    *)
        for ((i=1; i<=size; i++)); do
            printf "%d\n" $i >> $file
        done
        ;;
esac
