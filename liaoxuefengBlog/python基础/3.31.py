L = ['Bart', 'Lisa', 'Adam']

# i = 0
# while(i < len(L)):    #
#     print('Hello, ' + L[i] + '!')
#     i += 1

# for i in range(len(L)):
    # print('Hello, ' + L[i] + '!!')

n = 0
while n < 10:  # 打印奇数
    n += 1
    if (n % 2) == 0:
        n += 0  ## 这里可以用continue语句
    else:
        print(n)