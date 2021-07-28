n, m = map(int, input().split())

i = n

if n == m:
    for j in range(1, 10):
        print(f'{i}*{j}={i*j}')

else:
    while i <= m:
        for j in range(1, 10):
            print(f'{i}*{j}={i*j}')
        i += 1