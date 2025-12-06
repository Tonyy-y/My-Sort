#!/bin/bash
v=($(cat numbers.in))
len=${#v[@]}

#Cod pentru cazurile in care lungimea nu este o putere de a lui 2
putere=1
while (( putere<len )); do
    (( putere*=2 ))
done

VAL_MAX=9999999999

for (( i=len; i<putere; i++ )); do
    v[$i]=$VAL_MAX
done

bitonicSwap() {
    local i=$1
    local j=$2
    local dir=$3    #1 = Crescator; 0 = Descrescator;

    local val_i=${v[$i]}
    local val_j=${v[$j]}

    if [[ ($dir -eq 1 && $val_i -gt $val_j) || \
          ($dir -eq 0 && $val_i -lt $val_j) ]]; then
        
        v[$i]=$val_j
        v[$j]=$val_i
    fi
}

bitonicMerge() {
    local low=$1
    local count=$2
    local dir=$3    #1 = Crescator; 0 = Descrescator;

    if (( count > 1 )); then
        local k=$(( count/2 ))
        for (( i=low ; i < low+k; i++)); do
            bitonicSwap $i $(( i+k )) $dir
        done

        bitonicMerge $low $k $dir

        bitonicMerge $(( low+k )) $k $dir
    fi
}

bitonicSort() {
    local low=$1
    local count=$2
    local dir=$3    #1 = Crescator; 0 = Descrescator;
    
    if (( count > 1 )); then
        local k=$(( count/2 ))

        bitonicSort $low $k 1

        bitonicSort $(( low+k )) $k 0

        bitonicMerge $low $count $dir
    fi
}

#Apelam algoritmul crescator, de la 0 pana la cea mai mica putere a lui 2 >= decat len
bitonicSort 0 $putere 1

#Afisam doar numerele pana la lungimea sirului intial sortate
for (( i=0; i<len; i++)); do 
    printf "%d\n" ${v[i]}
done > numbers.out