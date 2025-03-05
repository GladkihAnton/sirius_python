from1 = int(input())
to1 = int(input())
from2 = int(input())
to2 = int(input())

for num1 in range(from1, to1 + 1):
    for num2 in range(from2, to2 + 1):
        print(num1, num2, num1 * num2, end="\n", sep="/")


'''
	5	6
7	35	42
8	40	48
9	45	54
10	50	60
'''
#
# 5 5
# 5 6
# 5 7
# 5 8
# 6 5
# 6 6
# 6 7
# 6 8
# 7 5
# 7 6
# 7 7
# 7 8
# 8 5
# 8 6
# 8 7
# 8 8
