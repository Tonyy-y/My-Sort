import subprocess
import matplotlib.pyplot as plt # type: ignore
import time
import random

times_shellSort = []
times_ciura = []
times_ciura225odd = []
times_knuth = []
times_tokuda = []

elements = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000]

#subprocess.run(['dos2unix', 'shellSort.sh', 'ciura.sh', 'ciura225odd.sh', 'knuth.sh', 'tokuda.sh'])

for i in elements:
    with open("numbers.in", "w") as f:
        random.seed(a=1776 + i, version=2)
        for j in range(i):
            x = random.randint(-77777, 77777)
            f.write(str(x) + "\n")

    start = time.perf_counter()
    subprocess.run(['./shellSort.sh', 'numbers.in', 'numbers.out'])
    times_shellSort.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    subprocess.run(['./ciura.sh', 'numbers.in', 'numbers.out'])
    times_ciura.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    subprocess.run(['./ciura225odd.sh', 'numbers.in', 'numbers.out'])
    times_ciura225odd.append(time.perf_counter() - start)

    start = time.perf_counter()
    subprocess.run(['./knuth.sh', 'numbers.in', 'numbers.out'])
    times_knuth.append(time.perf_counter() - start)

    start = time.perf_counter()
    subprocess.run(['./tokuda.sh', 'numbers.in', 'numbers.out'])
    times_tokuda.append(time.perf_counter() - start)

plt.figure(figsize=(16, 9))
runs = list(range(1, len(elements)+1))
plt.plot(runs, times_shellSort, marker='s', label='Classic Gap')
plt.plot(runs, times_ciura, marker='o', label='Ciura')
plt.plot(runs, times_ciura225odd, marker='D', label='Ciura-225-Odd')
plt.plot(runs, times_knuth, marker='^', label='Knuth')
plt.plot(runs, times_tokuda, marker='v', label='Tokuda')

y_all = times_shellSort + times_ciura + times_ciura225odd + times_knuth + times_tokuda
offset = max(y_all) * 0.01

for i, run in enumerate(runs):
    current_values = [(times_shellSort[i], "blue"), (times_ciura[i], "orange"), (times_ciura225odd[i], "green"), (times_knuth[i], "red"), (times_tokuda[i], "purple")]
    current_values.sort(key=lambda x: x[0])
    for rank, (val, col) in enumerate(current_values):
        shift = (rank - 2) * offset 
        plt.text(run, val + shift, f'{val:.2f}', fontsize=8, ha='center', va='center', color=col)

plt.xlabel('n (Numarul de elemente)', fontsize=12)
plt.ylabel('Timp (secunde)', fontsize=12)
plt.title('Performanta shellSort cu diferite gap-uri', fontsize=14)
plt.xticks(runs, elements, rotation=45)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
