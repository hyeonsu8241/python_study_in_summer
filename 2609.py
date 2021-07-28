n, m = map(int, input().split())
if 1<= n and n <= 10000 and 1 <= m and m <= 10000:
    max = 0
    tmp = 0
    if n > m:
        tmp = n; n = m; m = tmp

    for i in range(1, m + 1):
        if n % i == 0:
            if m % i == 0:
                max = i

    min = int(n * m / max)

    print(max)
    print(min)