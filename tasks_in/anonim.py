def temp(a, b):
    return a + b


func = lambda a, b: a + b

class User:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name


maksim = User(20, "maksim")
igor = User(25, "igor")
users = [maksim, igor]


def user_age(user):
    return user.age


print(max(users, key=lambda user: user.age).name)
for user in sorted(users, key=lambda user: user.age):
    print(user.name)
