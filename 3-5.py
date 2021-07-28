n, m = map(int, input().split())
count = 0
if 2 <= n and n <= 100000 and 2 <= m and m<= 100000:
    while n != 1:
        if n % m == 0:
            n //= m
            count += 1
        else:
            n -= 1
            count += 1

print(count)