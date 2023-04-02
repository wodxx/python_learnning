# list and tuple

## list

list 为一个数组

形式：   list = [index，index2，index3]

```py
1. len(list)  # 计算list的元素个数
2. len[0]    # 第一个元素 用索引来访问list中每一个位置的元素，索引是从0开始的。
3. list[-1]  # 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素： 取列表中的最后一个元素
4. list.append(value) # 往list中的末尾加一个元素
5. list.insert(index, value) # 往list指定位置插入元素 index表示索引位置
6. list.pop() # 删除list的末尾元素
7. list.pop(index) # 删除list中的指定元素，index为该元素的索引位置
8. list[1] = value # 替换list中索引位置1处的元素值
9. list可以嵌套，即list的元素也可以是一个list
```

## tuple

一种有序列表叫元组：tuple。tuple和list非常类似, **但是tuple一旦初始化就不能修改**，比如同样是列出同学的名字

classmates = ('Michael', 'Bob', 'Tracy')

1. 没有append()，insert()这样的方法,即不能增、删元组里面的元素。但可以正常索引，同list。

2. tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。**tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。指向的具体内容可以变**，如果元组中的一个元素是一个list，那么可以变这个list里的元素。

```PY
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X' # 改变元组中list的值是可以的
t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

3. 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义： t = (1,)