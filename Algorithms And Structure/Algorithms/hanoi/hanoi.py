#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/20 18:12



def hanoi(n, A, B, C):
	if n > 0:
		hanoi(n-1, A, C, B)
		print("%s -> %s\n"%(A, C))
		hanoi(n-1, B, A, C)
		


if __name__ == '__main__':
	hanoi(3, 'a', 'b', 'c')