N = int(input())
if 1 <= N and N <= 100:
    for i in range(N, 0, -1):
        star = '*' * i
        print(star.rjust(N))