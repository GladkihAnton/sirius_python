"""Напишите генератор words_from_sentence(sentence), который принимает строку и возвращает слова по одному."""

"""
gen = words_from_sentence("Раздели меня пробелами")
for word in gen:
    print(word)
"""

"""(!) Решение не должно использовать split, так как суть генератора тогда теряется"""

def words_from_sentence(sentence):
    print("START")
    result = ''
    for index in range(len(sentence)):
        if sentence[index] == ' ':
            yield result
            result = ''
        else:
            result += sentence[index]
    yield result
    return


print("BEFORE GEN")
gen = words_from_sentence("Раздели меня пробелами")
gen1 = words_from_sentence("Раздели меня пробелами")
print("AFTER GEN")
print(next(gen))
print(next(gen))
print(next(gen1))
