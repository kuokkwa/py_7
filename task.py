import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Tuple

random.seed(0)
np.random.seed(0)

def shell_sort_ops(arr: List[float]) -> Tuple[List[float], dict]:
    a = list(arr)
    n = len(a)
    comps = 0
    assigns = 0
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            assigns += 1
            j = i
            while j >= gap:
                comps += 1
                if a[j-gap] > temp:
                    a[j] = a[j-gap]
                    assigns += 1
                    j -= gap
                else:
                    break
            a[j] = temp
            assigns += 1
        gap //= 2
    return a, {"comparisons": comps, "assignments": assigns, "total": comps + assigns}

def merge_sort_ops(arr: List[float]) -> Tuple[List[float], dict]:
    a = list(arr)
    comps = 0
    assigns = 0
    
    def merge(left: List[float], right: List[float]) -> List[float]:
        nonlocal comps, assigns
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            comps += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                assigns += 1
                i += 1
            else:
                merged.append(right[j])
                assigns += 1
                j += 1
        while i < len(left):
            merged.append(left[i])
            assigns += 1
            i += 1
        while j < len(right):
            merged.append(right[j])
            assigns += 1
            j += 1
        return merged

    def msort(lst: List[float]) -> List[float]:
        if len(lst) <= 1:
            return lst[:]
        mid = len(lst) // 2
        left = msort(lst[:mid])
        right = msort(lst[mid:])
        return merge(left, right)

    sorted_a = msort(a)
    return sorted_a, {"comparisons": comps, "assignments": assigns, "total": comps + assigns}

Ns = list(range(100, 2001, 100))
repeat = 5
results = []

print("Початок експерименту...")

for N in Ns:
    times_shell = []
    ops_shell = []
    times_merge = []
    ops_merge = []
    
    for _ in range(repeat):
        data = [random.randint(0, 50) for _ in range(N)]
        
        # Shell Sort
        t0 = time.perf_counter()
        _, ops1 = shell_sort_ops(data)
        t1 = time.perf_counter()
        times_shell.append(t1 - t0)
        ops_shell.append(ops1["total"])
        
        t0 = time.perf_counter()
        _, ops2 = merge_sort_ops(data)
        t1 = time.perf_counter()
        times_merge.append(t1 - t0)
        ops_merge.append(ops2["total"])
    
    results.append({
        "N": N,
        "time_shell_avg": sum(times_shell)/repeat,
        "ops_shell_avg": sum(ops_shell)/repeat,
        "time_merge_avg": sum(times_merge)/repeat,
        "ops_merge_avg": sum(ops_merge)/repeat,
    })

df = pd.DataFrame(results)

pd.options.display.float_format = '{:,.4f}'.format
print("\nТаблиця результатів (перші 10 рядків):")
print(df[["N", "time_shell_avg", "ops_shell_avg", "time_merge_avg", "ops_merge_avg"]].head(10).to_string(index=False))

# Графік 1: Час виконання
plt.figure(figsize=(10, 6))
plt.plot(df["N"], df["time_shell_avg"], marker='o', label="Сортування Шелла (Shell Sort)")
plt.plot(df["N"], df["time_merge_avg"], marker='s', label="Сортування злиттям (Merge Sort)")
plt.xlabel("Розмір списку (N)")
plt.ylabel("Середній час (сек)")
plt.title("Залежність часу виконання від розміру списку")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Графік 2: Кількість операцій
plt.figure(figsize=(10, 6))
plt.plot(df["N"], df["ops_shell_avg"], marker='o', label="Shell Sort (Total Ops)")
plt.plot(df["N"], df["ops_merge_avg"], marker='s', label="Merge Sort (Total Ops)")
plt.xlabel("Розмір списку (N)")
plt.ylabel("Кількість елементарних операцій")
plt.title("Залежність кількості операцій від розміру списку")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

csv_path = "sort_experiment_results.csv"
df.to_csv(csv_path, index=False)
print(f"\nФайл з результатами збережено: {csv_path}")