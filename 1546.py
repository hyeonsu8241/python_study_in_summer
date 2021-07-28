N = int(input())
if N <= 1000:
    c_grade = list(map(int, input().split()))
    for i in c_grade:
        if i < 0 and i > 100:
            break
    c_grade.sort(reverse=True)

    M = c_grade[0]
    sum = 0
    for i in range(N):
        c_grade[i] = c_grade[i] / M * 100
        sum += c_grade[i]
    
    avr = float(sum / N)
    print(avr)