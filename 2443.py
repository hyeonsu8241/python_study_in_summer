N = int(input())

if 1 <= N and N <= 100:
    for i in range(1, N + 1):
        star = '*' * (2 * N - 2 * i + 1)
        print(star.center(2 * N - 1, ' '))