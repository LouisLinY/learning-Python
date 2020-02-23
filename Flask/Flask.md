Flask 

装饰器

Flask安装/架构

Routing

Http Method

静态和模板

Request/Response

Error/重定向

Flask Message

Logger

Flask-Script





装饰器--decorator

例子：

```python
def log(func):
    def wrapper():
        print('before calling', func.__name__)
        func()
        print('end calling', func.__name__)
    return wrapper

def hello():
    print("hello")
    
#带参数
def log(func):
    def wrapper(*args, **kvargs):
        print('before calling', func.__name__)
        func()
        print('end calling', func.__name__)
    return wrapper
    
    
    
    
def log(level, )
    
    
```











