class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __add__(self, other):
        newnum = self.numerator * other.denumerator + self.denumerator * other.numerator
        newden = self.denumerator * other.denumerator
        return Fraction(newnum // 2, newden // 2)

    def __sub__(self, other):
        newnum = self.numerator * other.denumerator - self.denumerator * other.numerator
        newden = self.denumerator * other.denumerator
        return Fraction(newnum // 2, newden // 2)

    def __mul__(self, other):
        newnum = self.numerator * other.denumerator * self.denumerator * other.numerator
        newden = self.denumerator * other.denumerator
        return Fraction(newnum // 2, newden // 2)

    def __floordiv__(self, other):
        newnum = self.numerator * other.denumerator * self.denumerator * other.numerator
        newden = self.denumerator // other.denumerator
        return Fraction(newnum // 2, newden // 2)


f1 = Fraction(3, 2)
f2 = Fraction(2, 4)
f3 = f1 + f2
print(f"{f3.numerator}/{f3.denumerator}")
