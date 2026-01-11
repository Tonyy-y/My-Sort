import subprocess
import math
import time
import random
import sys

try:
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("Instaleaza matplot lib\nFoloseste 'pip install matplotlib'")
    

def ceil_to_2_decimals(value):
    return math.ceil(value * 100) / 100

times_shellSort = []
times_bitonicSort = []
time_sort = []

numar_elemente = [int(x) for x in input("Introduceti numarul de elemente al sirurilor(cu spatiu intre ele)\nPentru valorile initiale lasati gol(16,128,1024,1026,2048,2079,4096,8000,10000,32768):  ").split()]
if not numar_elemente:
    numar_elemente = [16,128,1024,1026,2048,2079,4096,8000,10000,32768]

#number gen
for i in numar_elemente:
    with open("numbers.in", "w") as f:
        random.seed(a=129 + i, version=2)
        for j in range(i):
            x = random.randint(-99999999, 99999999)
            f.write(str(x) + "\n")
    
    # shellSort
    start = time.perf_counter()
    subprocess.run(['./shellSort.sh', 'numbers.in', 'numbers.out'])
    times_shellSort.append(ceil_to_2_decimals(time.perf_counter() - start))
    
    # bitonicSort
    start = time.perf_counter()
    subprocess.run(['./bitonicSort.sh', 'numbers.in', 'numbers.out'])
    times_bitonicSort.append(ceil_to_2_decimals(time.perf_counter() - start))
    
    # sort -n
    start = time.perf_counter()
    subprocess.run(['sort', '-n', 'numbers.in'], stdout=open('numbers.out', 'w'))
    time_sort.append(ceil_to_2_decimals(time.perf_counter() - start))

print("Times shellimp:", times_shellSort)
print("Times bit:", times_bitonicSort)
print("Times shell:", time_sort)

plt.figure(figsize=(16, 9))

#liniile graficului
runs = list(range(1, len(numar_elemente)+1))
plt.plot(runs, times_shellSort, marker='o', label='shellSort')
plt.plot(runs, times_bitonicSort, marker='s', label='bitonicSort')
plt.plot(runs, time_sort, marker='^', label='sort -n')

#offset pt text
y_range = max(max(times_shellSort), max(times_bitonicSort), max(time_sort))
offset = y_range * 0.03

#textul
for run, time_val in zip(runs, times_shellSort):
    plt.text(run, time_val, f'{time_val}', fontsize=14, ha='right', va='bottom', 
             rotation=45, color="#27287c")

for run, time_val in zip(runs, times_bitonicSort):
    plt.text(run, time_val + offset, f'{time_val}', fontsize=14, ha='left', va='bottom', 
             rotation=45, color="#6f3c17")

for run, time_val in zip(runs, time_sort):
    plt.text(run, time_val - offset, f'{time_val}', fontsize=14, ha='center', va='top', 
             rotation=0, color='green')
    
#graficul
plt.xlabel('Numarul de elemente', fontsize=24)
plt.ylabel('Timp (secunde)', fontsize=24)
plt.title(f'Performanta cu 10 siruri aleatorii de {numar_elemente} elemente', fontsize=30)
plt.xticks(runs, numar_elemente, rotation=45, fontsize=18)

plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
