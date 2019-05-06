
class complex:
    def __init__(self, r=0, j=1):
        self.r = r
        self.j = j

    def __add__(self, other):
        if isinstance(other, int):
            return complex(self.r + other, self.j)
        elif isinstance(other, complex):
            return complex(self.r + other.r, self.j + other.j)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, int):
            return complex(self.r / other, self.j / other)
        elif isinstance(other, complex):
            return complex((self.r * other.r + self.j * other.j) / (other.r*other.r + other.j*other.j), (self.j * other.r - self.r * other.j) / (other.r*other.r + other.j*other.j))
        else:
            raise TypeError

    def __float__(self):
        return float(self.r) / self.comp

    def __int__(self):
        return self.r / self.j

    def __mul__(self, other):
        if isinstance(other, int):
            return complex(other * self.r, other * self.j)
        elif isinstance(other, complex):
            return complex(((self.r * other.r) - (self.j * other.j)), ((self.j * other.r) + (self.r * other.j)))
        else:
            raise TypeError

    def __radd__(self, other):
        return self + other

    def __rtruediv__(self, other):
        return complex(other / self.r, 0 / self.j)

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return complex(other - self.r, 0 - self.j)

    def __str__(self):
        return '(' + str(self.r) + ") + (" + str(self.j) + ')i'

    def __sub__(self, other):
        if isinstance(other, int):
            return complex(self.r - other, self.j)
        elif isinstance(other, complex):
            return complex(self.r - other.r, self.j - other.j)
        else:
            raise TypeError

if __name__ == '__main__':

    a = complex(1, 2)
    b = complex(2, 3)

    i = 5

    
    print('%s + %s = %s' % (a, b, a + b))
    print('%s - %s = %s' % (a, b, a - b))
    print('%s * %s = %s' % (a, b, a * b))
    print('%s / %s = %s' % (a, b, a / b))

    print('%s + %i = %s' % (a, i, a + i))
    print('%s - %i = %s' % (a, i, a - i))
    print('%s * %i = %s' % (a, i, a * i))
    print('%s / %i = %s' % (a, i, a / i))

    print('%i + %s = %s' % (i, a, i + a))
    print('%i - %s = %s' % (i, a, i - a))
    print('%i * %s = %s' % (i, a, i * a))
    print('%i / %s = %s' % (i, a, i / a))

