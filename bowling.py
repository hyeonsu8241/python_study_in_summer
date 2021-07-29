N, M = map(int, input().split())

K = list(map(int, input().split()))

K.sort(reverse=True)

col = 0

if 1 <= N and N <= 1000 and 1 <= M and M <= 10:
    if 1 <= K[len(K) - 1] and K[0] <= M:
        for i in range(N - 1):
            for j in range(i + 1, N):
                if K[i] != K[j]:
                    col += 1
    print(col)