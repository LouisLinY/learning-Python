#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/21 19:50

from cal_time import cal_time

@cal_time
def bin_search(l,n):
	low = 0
	high = len(l)-1
	mid = 0
	while low <= high:
		mid = (low + high)//2
		if l[mid] == n:
			return mid
		elif l[mid] > n:
			high = mid - 1
		else:
			low = mid + 1
	return -1

@cal_time
def sys_search(li, val):
	try:
		return li.index(val)
	except:
		return -1



if __name__ == '__main__':
	print("hello world!\n")
	li = range(200000000)
	bin_search(li, 200000000)
	sys_search(li, 200000000)
	# print(bin_search([1, 3, 5, 7, 9, 11], 4))
	# print(bin_search([1, 3, 5, 7, 9, 11], 1))
	# print(bin_search([1, 3, 5, 7, 9, 11], 11))
	# print(bin_search([1, 3, 5, 7, 9, 11], 3))
