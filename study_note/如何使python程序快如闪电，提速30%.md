##### 如何使python程序快如闪电，提速30%

讨厌python的人总是说，他们不想使用它的原因之一是它很慢，不管使用什么编程语言，程序是快还是慢都在很大程度上取决于编写程序的开发人员，以及他们编写最优化快速程序的技能和能力。

那我们来看看如何提高python的程序性能，使它们变得非常快，在我们开始优化任何东西之前，我们首先需要找出（计时和性能分析）到底是代码的哪些部分减慢了整个程序（减慢程序的部分）？有时程序的瓶颈可能是显而易见的，但如果你不知道它在哪里，那么以下选项可以帮你找出来

例子：它是用于计算e的x次方

```python
#slow_program.py
from decimal import *
def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s!= lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num/fact
    getcontext().prec -= 2
    return +s

exp(Decimal(150))
exp(Decimal(400))
exp(Decimal(3000))
```

- 首先是最简单同时又非常懒惰的解决方案

​       使用Unix time命令，如果你只是想计算整个程序的运行时间，只需要这样做就行了，但这通常不能满足我们的需求，

```
time python3.8 slow_program.py
real 
user
sys
```

- 最详细的性能分析

  使用cProfile，但是它提供的信息又太多了，在这里我们使用cProfile模块和time参数运行测试脚本，这样就可以根据内部时间cumtime对代码进行排序，这给了我们很多信息，这里的内容大约是实际输出的10%，我们可以看到exp函数是罪魁祸首

  ```
  python3.8 -m cProfile -s time slow_program.py
  ```

  现在我们可以得到更具体的时间和性能分析，现在我们知道了应该将注意力放在哪里（对具体的函数计时），如果我们希望对慢速函数进行计时，而不需要测量代码的其余部分，可以使用简单的装饰器，把这个装饰器应用到函数上，然后进行输出，这里需要考虑的一件事是我们实际想测量的是哪种时间？时间包提供了time.perf_counter和time.process_time，它们的不同之处在于perf_counter返回绝对值（其中包括python程序进程不运行的时间，因此可能会受到机器负载的影响），另一方面process_time只返回用户时间，不包括系统时间，只是进程的时间，

  ```python
  def timeit_wrapper(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          start = time.perf_counter()  #Alternatively, you can use time.process_time
          func_return_val = func(*args, **kwargs)
          end = time.perf_counter()
          print('{0:<10}.{1:<8}: {2:<8}'.format(func.__module__, func.__name__, end-start))
          return func_return_val
      return wrapper
  ```

  ```
  @timeit_wrapper
  def exp(x):
      ....
      
  print('{0:<10} {1:<8} {2:^8}'.format('module', 'function', 'time'))
  ```

  ```
  python3.8 slow_program.py
  ```

  

那么有趣的部分来了，让我们将你的python程序运行的更快一些吧，需要注意的时，这里不会向你展示骇客技术、技巧和代码片段，更多介绍的是一般的想法和策略，当你使用它们时，会对性能产生巨大的影响，在某些情况下可以提高30%的速度，

- 第一点 使用内置数据类型，内置数据类型非常快，特别是与树和链表等自定义类型相比，这主要是因为内置类型是用c实现的，我们无法在速度上与之匹配；

- 第二点 使用lru_cache缓存数据

  这里通过一个简单的例子说明一下，这里的函数使用time.sleep模拟大量计算，第一次使用参数1调度时，它等待2秒，然后才返回结果，当再次调用时，结果已经被缓存，因此它会跳过函数体并立即返回结果，更多例子https://mobile.twitter.com/raymondh/status/1205969258800275456

  ```python
  import functools
  import time
  #最多缓存12个不同的结果
  @functools.lru_cache(maxsize=12)
  def slow_func(x):
      time.sleep(2) #模拟长时间计算
      return x
  slow_func(1) #...等待2秒才能获得结果
  slow_func(1) #结果一缓存，会立即返回
  slow_func(3) #...等待2秒才能获得结果
  ```

- 第三点 使用局部变量

  这与在每个作用域内查找变量的速度有关，在这里，写每个作用域是因为它不只关乎是使用局部变量还是全局变量，查找速度也存在着差异，在函数中的局部变量最快，类级属性次之，而全局变量最慢，可以像这样，使用不必要的赋值来提升性能

  ```python
  #示例1
  class FastClass:
      def do_stuff(self):
          temp = self.value  #这可以加速循环中的查找
          for i in range(10000):
              ... #在这里使用‘temp’做一些操作
              
  #示例2
  import random
  def fastfunction():
      r = random.random
      for i in range(10000):
          print(r())  #在这里调用‘r()’, 比全局的random.random()要快
  ```

  

- 使用函数

  这看起来可能不符合直觉，因为调用函数会将更多的东西放到堆栈中，从函数返回时会产生开销，但这与前面一点有关，如果你只是将整个代码放入一个文件中，而不将其放入函数中，那么由于全局变量的关系，速度会慢很多，因此你只是将整个代码封装在main函数中并调用一次，就可以加快代码

  ```
  def main():
      ... #之前所有的全局代码
  main()
  ```

- 不要访问属性

  另一个可能降低程序速度的是点操作符(.)，它用于访问对象属性

  

  

  ```python
  
  ```

  

- 11

- 

