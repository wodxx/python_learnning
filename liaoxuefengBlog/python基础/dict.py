d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d.get('wuxuhui'))   # 查找,结果为none

if 'wxh' in d:  # 查找
    print('yes')
else:
    print('no')

d.pop('Bob') # 删除操作

print(d)