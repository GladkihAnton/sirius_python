word = input()

current_letter = word[0]
current_len = 1
result = ""
for index in range(1, len(word) - 1):
    next_letter = word[index + 1]

    print(f'{index=}')
    if current_letter == next_letter:
        print(f'EQUAL: {current_letter=}//{current_len=}//{next_letter=}')
        current_len += 1
    else:
        print(f'UNEQUAL: {current_letter=}//{current_len=}//{next_letter=}')
        result += f'{current_letter}{current_len}'
        current_len = 1
        current_letter = next_letter


print(result + f'{current_letter}{current_len}')