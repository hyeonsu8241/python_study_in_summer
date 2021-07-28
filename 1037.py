N = int(input())
if 1 <= N and N <= 50:
    measure = list(map(int, input().split()))

    number = measure[0] * measure[N - 1]
    print(number)