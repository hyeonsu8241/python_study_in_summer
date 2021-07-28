N = int(input())
count = 0

def decimal(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        return count

if 1 <= N and N <= 100:
    num = [None] * N
    num = map(int, input().split())
    for i in range(num):
        if decimal(i) == 0:
            count += 1
    print(count)
