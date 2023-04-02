# dict & set

## dict

> Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

### 形式: 

```py
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

d['Michael']

95
```

### 往一个dict中加入元素,用key的方法

```py
d['Adam'] = 67   # 往d中加入一个键值对,dict的名字后用中括号写key,等号对应的是value

d['Adam']

67

## 注:由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
```

### 查找一个key是否存在
方法一:

```py
'Thomas' in d

False
# 用 key in dict 语法
```

方法二:通过dict提供的**get()方法**，如果key不存在，可以返回None，或者自己指定的value：

```py
d.get('Thomas')

d.get('Thomas', -1)

-1
# 返回None的时候Python的交互环境不显示结果
```

### 删除一个key

用pop(key)方法，对应的value也会从dict中删除
```py
d.pop('Bob')

75

d

{'Michael': 95, 'Tracy': 85}
```

### 与list比较

请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

1. 查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

2. 而list相反,查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。

所以，**dict是用空间来换取时间**的一种方法;且需要注意,dict的key必须是不可变对象.


## set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：

```py
s = set([1, 2, 3])

s

{1, 2, 3}
```

注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是说明这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

### 重复元素在set中自动被过滤

```py
s = set([1, 1, 2, 2, 3, 3])

s

{1, 2, 3}
```

### 增加元素 add(key)

```py
s.add(4)

s

{1, 2, 3, 4}

## 重复添加不会有效果
```

### 通过remove(key)方法可以删除元素
```py
s.remove(4)

s

{1, 2, 3}
```

> set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

> set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。