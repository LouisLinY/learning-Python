python高级编程

魔法函数

```python
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    def __len__(self):
        return len(self.employee)
    
    
company = Company(["tomcat", "java", "python"])


```



深入类和对象

鸭子类型和多态

```python
class Cat(object):
    def say(self):
        print("i am a cat")
   
class Dog(object):
    def say(self):
        print("i am a dog")
        
class Duck(object):
    def say(self):
        print("i am a duck")
        
animal = Cat
animal().say()


#多态，所有的子类必须继承父类 

```

​    抽象基类

#java接口，无法实现多继承的，只能继承一个类，但是可以继承多个接口，接口不能用来实例化的，python抽象基类不能实例化的

动态语言没有变量的类型

 





