N = int(input())
if 1<= N and N <= 1000000:
    num = [0] * N
    num = list(map(int, input().split()))

    num.sort()
    print(num[0], num[N - 1])