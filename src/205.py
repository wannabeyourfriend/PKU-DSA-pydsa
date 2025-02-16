### Python官方的数据结构复杂度网站

### https://wiki.python.org/moin/TimeComplexity




#讨论一下Python两个内置的数据结构list和dict的时间复杂度:
from timeit import Timer
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# 列表推导式comprehension
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

# list.pop()的计时实验
import timeit
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))
x = list(range(2000000))
print(popend.timeit(number=1000))

"""
设计一个性能试验来验证list中检索一个
值,以及dict中检索一个值的计时对比
生成包含连续值的list和包含连续关键码key的dict,用随机数来检验操作符in的耗时
"""
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)} # 字典推导式，生成键为整数，值为None的字典
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))

    
