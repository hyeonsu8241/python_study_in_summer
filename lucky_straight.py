N = int(input())

if 10 <= N and N <= 99999999:
    n = list(map(int, str(N)))
    if len(n) % 2 == 0:

        center = int(len(n) / 2)

        sum_left = 0
        sum_right = 0

        for i in range(center):
            sum_left += n[i]

        for i in range(center, len(n)):
            sum_right += n[i]

        if sum_left == sum_right:
            print('LUCKY')
        elif sum_left != sum_right:
            print('READY')