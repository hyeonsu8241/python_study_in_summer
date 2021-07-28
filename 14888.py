class Calculator:
    def __init__(self):
        self.result = 0

    def plus(self, item):
        return self.result + item

    def minus(self, item):
        return self.result - item

    def mul(self, item):
        return self.result * item

    def div(self, item):
        return self.result // item

N = int(input())
result = Calculator()
if 2 <= N and N <= 11:
    a = list(map(int, input().split()))
    plus, minus, mul, div = map(int, input().split())
    result += a[0]
    for i in range(len(a) - 1):
        