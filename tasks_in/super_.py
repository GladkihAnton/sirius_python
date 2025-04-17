
class ParentParent1:
    def temp(self):
        print('parent_parent1')


class ParentParent2:
    def temp(self):
        print('parent_parent2')


class ParentParent3:
    def temp3(self):
        print('parent_parent3')


class Parent(ParentParent1, ParentParent2):
    def temp(self):
        print('parent')


class Parent1(ParentParent2, ParentParent3):
    def temp(self):
        print('parent1')


class Parent2:
    def temp(self):
        print('parent2')


class Parent3:
    def temp(self):
        print('parent3')


class X(Parent, Parent1, Parent2, Parent3):
    def temp(self):
        print('x')
        super(Parent, self).temp()  # find in ParentParentX


class BaseUser:
    def __init__(self, name, age):
        print('Init base user')
        self.name = name
        self.age = age


class Student(BaseUser):
    def __init__(self, name, age, score):
        print('Init student')
        super().__init__(name, age)
        print('after super')
        self.score = score


s = Student(name='John', age=20, score=1)
print(s.age)
print(s.score)
print(s.name)
