# Дан целочисленный массив nums и целое число k. Верните true, если в массиве есть два разных индекса i и j, таких что nums[i] == nums[j] и abs(i - j) <= k.

#
nums = [1, 2, 3, 1, 2, 3]

k = 4

for index in range(len(nums)):
    unique_numbers = set()
    window=nums[index:index+k]
    for window_index in range(len(window)):
        if window[window_index] in unique_numbers:
            print(True)
        else:
            unique_numbers.add(window[window_index])