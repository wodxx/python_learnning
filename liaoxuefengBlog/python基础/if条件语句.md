# if

if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

## input()函数

```python
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
## 输入98，报错。
## 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数

s = input('birth: ')
birth = int(s) # 数据类型的转换，转为什么就用什么函数，int()将其他类型转为整型
if birth < 2000:
    print('00前')
else:
    print('00后')
```