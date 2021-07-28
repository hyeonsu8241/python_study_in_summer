S = int(input())
n = 1
if 1 <= S and S <= 4294967295:
    while n * (n + 1) / 2 <= S:
        n += 1

    print(n - 1)