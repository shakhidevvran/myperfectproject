class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print('method __add__ called')
        self.num += other
        return Num(self.num)

    def __sub__(self, other):
        print("method sub called")
        self.num -= other
        return Num(self.num)

    def __str__(self):
        return f'Num: {self.num}'

    def __repr__(self):#дандер метод
        return f'Num({self.num})'


num1 = Num(20)
num2 = num1 + 20 - 30
print(repr(num2))




