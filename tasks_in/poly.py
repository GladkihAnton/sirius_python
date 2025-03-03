from typing import Any


class Iterator:

    def __next__(self) -> Any:
        raise NotImplementedError


class Iterable:
    def __iter__(self) -> Iterator:
        raise NotImplementedError


class ListIterable(Iterable):
    def __iter__(self):
        ...


class ListIterator(Iterator):
    def __next__(self):
        ...


if __name__ == "__main__":
    my_list: Iterable = [list(), dict()]
