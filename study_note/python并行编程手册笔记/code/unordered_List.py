#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/22 14:46

"""
一种数据项按照相对位置存放的数据集，特别的，被称为“无序表 unordered list”其中数据项只按照存放位置来索引
数据项之间只有位置之间的关系，对于位置的索引，内容没有什么特别的安排
抽象数据类型：无序表unorderd list
无序列表的操作如下：
List()：创建一个空表
add(item)：添加一个数据项到列表中，假设item原先不存在于列表中
remove(item)：从列表中移除item，列表被修改，item原先应存在于列表中
search(item)：在列表中查找item，返回布尔类型
isEmpty()：返回列表是否为空
size()：返回列表包含了多少数据项
append(item):添加一个数据项到表末尾，假设item原先不存在于列表中
index(item)：返回数据项在表中的位置
insert(pos, item)：将数据项插入到位置pos，假设item原先不存在于列表中，同时原先列表具有
足够多个数据项，能让item占据位置pos
pop()：从列表末尾移除数据项，假设原先列表至少有1个数据项
pop(item)：移除位置为pos的数据项，假设原列表存在位置pos

采用链表实现无序表
为了实现无序表数据结构，可以采用链接表的方案
虽然列表数据结构要去保持数据项的前后相对位置，但这种前后位置的保存，并不要求数据项依次存
放在连续的存储空间
数据项存放位置并没有规则，但如果在数据项之间建立链接指向，就可以保存其前后相对位置

队首：链表的链首我们要给它记住
队尾：链表的尾巴，要做特殊标记，没有别的数据

链表实现：节点Node
链表实现的最基本元素时节点Node
每个节点至少要包含2个信息：数据项本身，以及指向下一个节点的引用信息
next为None的意义是没有下一个节点了

链表实现：无序表Unorderedlist
可以采用链接节点的方式构建数据集来实现无序表
链表的第一个和最后一个节点最重要
如果想要访问到链表中的所有节点，就必须从第一个节点开始沿着链表遍历下去，直到
next为空（None）
所以无序表必须要有对第一个节点的引用信息
设立一个属性head，保存对第一个节点的引用，空表的head为None

随着数据项的加入，无序表的head始终指向链表中的第一个节点
无序表对象本身并不包含数据项，数据项在节点中
其中包含的head只是对首个节点Node的引用
判断空表的isEmpty()很容易实现

考虑如何实现向无序表中添加数据项，实现add方法
由于无序表并没有限定数据项之间的顺序
新数据项可以加入到原表的任何位置
按照实现性能考虑，应添加到最容易加入的位置上

由链表结构可以知道
要访问到整个链表上的所有数据项
都必须从表头head开始沿着next链表逐个向后查找
所以添加新数据项（节点）最快捷的位置是表头，整个链表的首位置。

"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        """
        在表头添加数据，O（1）
        顺序表中insert(0, item) O（n）
        :param item:
        :return:
        """
        # if isEmpty(self):
        #     self.head = newnode
        # else:
        #     newnode.next = head
        #     self.head = newnode
        temp  = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """
        从链表头head开始遍历到链表表尾同时用变量累加经过的节点个数O（n）
        顺序表：最后一项地址减掉第一个数据项地址，然后除以数据项的大小O（1）
        :return: count
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """
        从链表头head开始遍历到表尾，同时判断当前节点的数据是否是目标
        :param item:
        :return:
        """
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """
        首先要找到item，这个过程跟search一样，但删除节点时，需要特别的技巧
        current指向的是当前匹配数据项的节点
        而删除需要把前一个节点的next执行current的下一个节点
        所以在search current的同时，还要维护前一个previous节点的引用
        找到item之后，current指向item节点，previous指向前一个节点，开始执行删除，
        需要区分两种情况：
        current是首个节点;或者位于链表的中间节点
        :param item:
        :return:
        """
        current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                break
            else:
                previous = current
                current = current.getNext()

        """
        教学实现
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        """








# if __name__ == '__main__':
