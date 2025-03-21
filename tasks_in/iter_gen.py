def recurs_(n: int):
    print(f'step before {n=}')
    if n == 3:
        return n-1
    results = recurs_(n-1)
    print(f'step after {n=}')
    return results


def gen_recurs(n: int):
    for i in range(n):
        print('step before', i)
        yield i
        print('step after', i)

print(type(recurs_))
iterator = gen_recurs(5)
print(next(iterator))

# for gen_index in gen_recurs(10):
#     print(f'{gen_index=}')
