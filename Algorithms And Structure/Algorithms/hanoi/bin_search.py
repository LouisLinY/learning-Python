#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/20 18:37

def bin_search(l,n):
	low = 0
	high = len(l)

	mid = 0
	while low < high:
		mid = (low + high)//2
		if l[mid] == n:
			return mid
		elif l[mid] > n:
			low = mid - 1
		else:
			high = mid + 1
	return -1

if __name__ == '__main__':
	print(bin_search([1, 3, 5, 7, 9, 11], 4))
	print(bin_search([1, 3, 5, 7, 9, 11], 1))
	print(bin_search([1, 3, 5, 7, 9, 11], 11))
	print(bin_search([1, 3, 5, 7, 9, 11], 3))
	