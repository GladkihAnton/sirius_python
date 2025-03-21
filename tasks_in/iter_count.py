'''Напишите класс Countdown, который будет представлять собой итератор для обратного отсчета.'''

'''
class Countdown:
    ...

countdown = Countdown(5)
for num in countdown:
    print(num)
'''


class Countdown:
    def __iter__(self):
        return self

    def __next__(self):
        result=self.count
        if self.count==0:
            raise StopIteration
        self.count-=1
        return result

    def __init__(self, count):
        print(count)
        self.count = count


countdown = Countdown(5)
countdown.count
for num in countdown:
    print(num)
