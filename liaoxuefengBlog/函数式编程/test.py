import builtins
import string
from functools import reduce

# 函数中传入一个函数作参数
# 且传入的函数只需传入函数本身

# def add_func(x, y, f):
#     return f(x) + f(y)

# print(add_func(5, -6, abs))


#######################################################
# [test1]: 改正不规范的人名书写

# def normalize(name):
#     pass
#     return str.capitalize(name)

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

#####################################################
#【test2】Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# def prod(L):
#     def cal(x, y):
#         return x * y
#     return reduce(cal, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# # 测试案例中传入的参数是一个list，所以结果最后返回的是reduce函数

# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

########################################################
#[test3]回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    str1 = str(n)  # 将一个整数转换为一个可迭代的字符串
    
    # i = 0    # 双指针法
    # j = len(str1)
    
    # while i != j :
    #     if str1[i] == str[j - 1] :
    #         i += 1
    #         j -= 1
    #     else:
    #         return False
        
    # return True

    str2 = str1[::-1]  # 反转法

    if str1 == str2 :
        return True
    else:
        return False

# 测试
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('successful!')
else:
    print('lose!')
