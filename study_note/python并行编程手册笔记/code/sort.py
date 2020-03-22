#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/22 10:17

import random
from cal_time import *

"""
列表排序
将无序列表变为有序列表

升序与降序
稳定性

排序低效：
冒泡排序
选择排序
插入排序

排序高效：
快速排序
堆排序
归并排序

排序不稳定排序：
基数排序
希尔排序
桶排序
*计算排序

"""
@cal_time
def bubble_sort(li):
    """
    首先，列表每两个相邻的数，如果前边的比后边的大，那么交换这两个数
    :param li:
    :return:
    """
    for i in range(len(li)-1):  #i表示第n趟， 一共n或者n-1趟
        for j in range(len(li)-1-i): #第i趟，无序区（0， n-i-1），j表示箭头0~n-i-2
            if li[j]> li[j+1]:
                li[j], li[j+1] =  li[j+1],  li[j]


def bubble_sort_update(li):
    """
    如果冒泡排序中执行一趟而没有交换，则列表已经是有序状态，可以直接结束算法
    最好情况O(n)，平均情况O(n^2)，最坏情况O(n^2)
    :param li:
    :return:
    """
    for i in range(len(li)-1):  #i表示第n趟， 一共n或者n-1趟
        exchange = False
        for j in range(len(li)-1-i): #第i趟，无序区（0， n-i-1），j表示箭头0~n-i-2
            if li[j]> li[j+1]:
                li[j], li[j+1] =  li[j+1],  li[j]
                exchange = True
        if not exchange:
            break


def get_min(li):
    min_pos = 0
    for i in range(1, len(li)):
        if li[i] < li[min_pos]:
            min_pos = i
    return min_pos


def search_sort(li):
    """
    一趟遍历记录最小的数，放到第一个位置
    在一趟遍历记录剩余列表中的最小的数，继续放置
    不稳定排序
    :return:
    """
    for i in range(len(li)-1):
        min_pos = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]


def insert_sort(li):
    """
    列表被分为有序区和无序区两部分，最初有序区只有一个元素
    每次从无序区选择一个元素，插入有序区的位置，直到无序区变空
    :param li:
    :return:
    """
    for i in range(1, len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        #j位置在循环结束的时候要么是-1要么是一个比tmp小的值
        li[j+1] = tmp


if __name__ == '__main__':
    li = list(range(10000))
    # random.shuffle(li)
    bubble_sort(li)