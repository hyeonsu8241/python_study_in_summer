from typing import Sequence

def max_of(a: Sequence) -> int:
    i = 0
    k = 0
    max = a[0]
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
            k += 1
    return max, k

k = 0
N = int(input())
if 1 <= N and N <= 100000:
    sum = 0
    x = [0] * N
    for i in range(N):
        x[i] = int(input())
    
    for i in range(N):
        if x[i] == 0:
            k += 1
    
    for i in range(N):
        if 1 <= x[i]:
            x.append(x[i])
        elif x[i] == 0:
            pr_thing, idx = max_of(x)
            print(pr_thing)
            x[idx] = 0

    for i in range(N):
        sum += x[i]
    
    if sum == 0:
        print(0)            

    