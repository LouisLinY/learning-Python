#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/22 16:29

"""
抽象数据类型：有序表OrderedList
有序表是一种数据项依照其某可比性质（如整数大小、字母表先后）来决定在列表中的位置

越小的数据项越靠近列表的头，越靠前

OrderedList所定义的操作如下：
OrderedList()：创建一个空的有序表
add(item)：在表中添加一个数据项，并保持整体顺序，此项原不存在
remove(item)：从有序表中移除一个数据项，此项应存在，有序表被修改
search(item)：在有序表中查找数据项，返回是否存在
isEmpty()：是否空表
index(item)：返回数据项在表中的位置，此项应存在
pop()：移除并返回有序表中最后一项，表中应该至少存在一项
pop(pos)：移除并返回有序表中指定位置的数据项，此位置应存在

在实现有序表的时候，需要记住的是，数据项的相对位置，取决于他们之间的“大小”
比较
由于Python的扩展性，下面对数据项的讨论并不仅适用于整数，可适用于所有定义了__gt__
方法的数据类型

同样采用链表方法实现
Node定义相同
OrderedList也设置一个head来保存链表头的引用
对于isEmpty/size/remove这些方法，与节点的次序无关，所以
其实现跟无序列表是一样的

search/add方法则需要有修改
search方法
在无序列表的search中，如果需要查找的数据项不存在，则会搜索
遍历整个链表，直到表尾
对于有序表来说，可以利用链表节点游戏排列的特性，来为search节
省不存在数据项的查找时间
一旦当前节点的数据项大于所要查找的数据项，则说明链表后面已经
不可能再有要查找的数据项，可以直接返回False


链表实现的算法分析
链表实现的list，跟python内置的列表数据类型，在有些相同方法
的实现上的时间复杂度不同
主要是因为python内置的列表数据类型是基于顺序存储来实现的，
并进行了优化
"""
from unordered_List import *

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        因为add方法必须保证加入的数据项添加在合适的位置，
        以维护整个链表的有序性
        由于涉及到插入位置是当前节点之前，而链表无法得到“前驱”
        节点的引用
        所以要跟remove方法类型，引入一个previous的引用，跟随当前节点current
        一旦找到首个比31大的数据项，previous就派上用场了
        :param item:
        :return:
        """
        current = self.head
        previous = None
        stop =False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)




    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if curretn.getData() == item:
                found = True
            else:
                if current.getData()>item:
                    stop = True
                else:
                    current = current.getNext()
        return found










