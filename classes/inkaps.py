
class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self._email = email
        self.__password = password

    def password(self):
        return hash(self.__password)


if __name__ == '__main__':
    user = User('<NAME>', '<EMAIL>', '<PASSWORD>')
    print(user.name)
    print(user._email)
    print(user._User__password)
