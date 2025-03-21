def new_number(num1, num2, num_list):
    if num2 > 100:
        return num_list
    num_list.append(num1 + num2)
    return new_number(num2, num1 + num2, num_list)

print(new_number(1, 1, []))