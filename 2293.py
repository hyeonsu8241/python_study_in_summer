n, k = map(int, input().split())
coin = [0] * n
if 1 <= n and n <= 100 and 1 <= k and k <= 10000:
    for i in range(n):
        coin[i] = int(input())