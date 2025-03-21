tuple_ = tuple()
list_ = []


def add_name(names=None):
    if names is None:
        names = []
    names.append("Name")
    print(names, id(names))


def wrong_add_name(names=[]):
    names.append("Name")
    print(names, id(names))


if __name__ == '__main__':
    first_list = []
    a = add_name()
    print(a)
    add_name(names=first_list)
    add_name(names=first_list)
    add_name()
    add_name(names=first_list)
    print(f'{first_list=}')
    print()
    print()
    print()
    print()
    second_list = []
    wrong_add_name()
    wrong_add_name(names=second_list)
    wrong_add_name(names=second_list)
    wrong_add_name()
    wrong_add_name(names=second_list)
    print(f'{second_list=}')
