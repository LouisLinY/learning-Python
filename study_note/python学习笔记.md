###### 1、函数及递归

任何递归函数都应该是这样的分情况处理：基本情况直接给出结果，一般情况通过递归处理，把对较“复杂”参数的计算归结为对较“简单”参数的计算，才能保证得到结果（保证函数定义的有效性）。

```python
def power(x, n):
    return 1 if n==0 else x*power(x, n-1)
```

python对程序执行中的最大函数调用深度有默认限制。例如：

power(2,1000)

通过sys标准库的函数getrecursionlimit()检查系统的调用深度上限，setrecursionlimit(n)把调用深度的上限设置为n

两个基本情况，出现两个递归项，称为二路递归

```python
def fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

标准库**timeit**可以方便完成各种计时，另外**cProfile**和**profile**包可用于统计程序中各部分的耗时

```python
def fib(n):
    if n < 0:
        return 0
    f1, f2 = 0, 1
    k = 0
    while k < n:
        f1, f2 = f2, f2 + f1
        k += 1
    return f1    
    
```





