#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/22 9:50

//尾递归的效率接近循环，python没有尾递归，能用循环的尽量用循环

def bin_search_rec(data_list, val, low, high):
    if low <= high:
        mid = (low+high)//2
        if data_list[mid] == val:
            return mid
        elif data_list[mid] > val:
            return bin_search_rec(data_list, val, low, mid-1)
        else:
            return bin_search_rec(data_list, val, mid+1, high)
    else:
        return -1



if __name__ == '__main__':
    print(bin_search_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 0, 9))
    print(bin_search_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 0, 9))
    print(bin_search_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0, 9))
    print(bin_search_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 0, 9))