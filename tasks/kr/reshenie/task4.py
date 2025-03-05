string = input()
substring_to_find = input()

result = 0
for index in range(len(string)):
    # abcd
    main_substring = string[index:index + len(substring_to_find)]
    print(f'{main_substring=}//{substring_to_find=}')
    if main_substring == substring_to_find:
        result += 1

print(result)
