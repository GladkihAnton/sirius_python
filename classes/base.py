user = {
    'name': 'name',
    'age': 10,
}


class Complex:
    def __init__(self, re: int, im: int) -> None:
        self.re = re
        self.im = im

    def __add__(self, other):
        # self == complex_1
        # other == complex_2
        print("__add__")
        print(f'{self=} {other=}')
        return Complex(re=self.re + other.re, im=self.im + other.im)

    def __repr__(self):
        return f'I"m Complex: re={self.re}. im={self.im}'


if __name__ == '__main__':
    complex_1 = Complex(1, 2)
    complex_2 = Complex(2, 3)
    print('START')
    complex_3 = complex_1 + complex_2
    print(f'{complex_3=}')
