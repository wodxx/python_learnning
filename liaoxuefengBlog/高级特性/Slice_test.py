import math
import sys
# 将一个字符串加入列表中

# string = 'ABCDEFG'

#length = len(string)

# list_string = []

# for i in string:
#     list_string.append(i)

# for i in range(length):
#     list_string.append(i)

# print(list_string)

#print(string[: : 2]) # 字符串切片

# string1 = ' ABCDEFG '  # 首尾带空格的字符串

# string2 = string1[1 : -2]

# print(string1[-1])

# print(string1)
# print(string2)


###########################################################
#【test1】去掉一个字符串首位的空格


# def trims(string):

#     if len(string) == 0:
#         return string
    
    
#     while string[:1] == ' ':     # 去掉首部空格
#         string = string[1:]
    
#     while string[-1:] == ' ':    # 去掉尾部空格
#         string = string[:-1]

#     if len(string) == 0:
#         return string
    
#     return string 

#  print(trims(' abc')) # 测试

#####################################################
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple

# def findMinAndMax(L1):

#     if len(L1) == 0:
#         return (None, None)

#     maxx = L1[0]
#     minx = L1[0]

#     for i in L1:
#         if i > maxx:
#             maxx = i

#     for j in L1:
#         if j < minx:
#             minx = j

#     return (minx, maxx)


# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('cscg!')

##################################################
# Fibonacci数列

def fib(max):
    # n = 0
    # a = 0
    # b = 1

    # while n < max:

    #     print(b)
    #     a, b = b, a + b
    #     n = n + 1

    # return 'done'
    
    if (max == 1) or (max == 2):
        return 1

    return fib(max - 1) + fib(max - 2)        
    
print(fib(6))