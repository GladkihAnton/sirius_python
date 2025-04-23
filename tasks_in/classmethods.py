import numpy as np
np.copy()



class X:
    def __init__(self, name):
        self.name = name

    def common(self):
        print('common')

    @classmethod
    def create_with_name_test(cls):
        return cls(name='test')

    @staticmethod
    def add_number(a, b):
        return a + b


print(id(X))
x = X.create_with_name_test()
# X.classmethod()
x = X('aaa')
x.common()
# x.classmethod()

X.add_number(1,2)

a = dict()
b = {"a": 1}

b = {1: None, 2: None}
c = dict.fromkeys([1, 2, 3, 4])
d = set([1,2,3,4])
print(c.keys(), d)