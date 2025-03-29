# Даны массив целочисленных значений nums и целое число target, верните индексы двух таких чисел, которые в сумме равны target.
#
# Гарантируется, что каждый ввод имеет ровно одно решение. Также учтите, что вы не можете использовать одно и то же число дважды.
#
# Вы можете вернуть ответ в любом порядке.
#
# Пример 1:
# ```
# Ввод: nums = [2,7,11,15], target = 9
# Вывод: [0,1]
# Пояснение: Так как nums[0] + nums[1] == 9, мы возвращаем [0, 1].
# ```
# Пример 2:
# ```
# Ввод: nums = [3,2,4], target = 6
# Вывод: [1,2]
# ```
# Пример 3:
# ```
# Ввод: nums = [3,3], target = 6
# Вывод: [0,1]
# ```
nums =[1, 2, 3, 10, 1000]
target = 1003

# O(n ^ 2)
# for index in range(len(nums)):
#     for index2 in range(index+1, len(nums)):
#         if nums[index] + nums[index2] == target:
#             print(index, index2)

# O(n log n)
# nums.sort()
# right_index = len(nums) - 1
# left_index = 0
# while nums[left_index] + nums[right_index] != target:
#     if nums[left_index] + nums[right_index] > target:
#         right_index -= 1
#     else:
#         left_index += 1
# print(left_index, right_index)

# O(n)
value_to_index = dict()
for i in range(len(nums)):
    value_to_find = target - nums[i]
    if value_to_find in value_to_index:
        j = value_to_index[value_to_find]
        print(j, i)
    value_to_index[nums[i]] = i
    print(f'{value_to_find= } {value_to_index=} v = {nums[i]}')