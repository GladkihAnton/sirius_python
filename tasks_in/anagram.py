'''
Даны две строки s и t, верните true, если t является анаграммой s, иначе верните false.

Анаграмма - это слово или словосочетание, образованное путем перестановки букв, составляющих другое слово (или словосочетание), обычно с использованием всех исходных букв ровно один раз.



Пример 1:

Ввод: s = "anagram", t = "nagaram"
Вывод: true
Пример 2:

Ввод: s = "rat", t = "car"
Вывод: false
'''
s = "anagramo"
t = "nagaramd"
dict1 = {}
dict2 ={}
for index in range(len(s)):
    if s[index] not in dict1.keys():
        dict1[s[index]] = 1
    else:
        dict1[s[index]] += 1
print(dict1)
for index in range(len(t)):
    if t[index] not in dict2.keys():
        dict2[t[index]] = 1
    else:
        dict2[t[index]] += 1
print(dict2)
print(dict1==dict2)
