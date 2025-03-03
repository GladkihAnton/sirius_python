hash_func = len


class Storage:
    def __init__(self):
        self.__storage = {}

    def put(self, key, value):
        key = hash_func(key)
        self.__storage[key] = value

    def get(self, key):
        key = hash_func(key)
        return self.__storage[key]


storage = Storage()
