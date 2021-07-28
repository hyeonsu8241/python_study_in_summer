N, K = map(int, input().split())

num = list(); count = 0

if 1 <= N and N <= 10000 and 1<= K and K <= N:
    for i in range(1, N + 1):
        if N % i == 0:
            num[count] = i; count += 1

if count < K - 1:
    print(0)

print(num[count])