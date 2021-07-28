def factorial(num: int) -> int:
    if num <= 1:
        return 1
    return num * factorial(num - 1)

N = int(input())
if 0 <= N and N <= 12:
    print(factorial(N))