#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/1 21:23

class Queue():
	def __init__(self):
		self._items = []
	
	def isEmpty(self):
		return self._items == []
	
	def enqueue(self, item):
		self._items.insert(0, item)
		
	def dequeue(self):
		return self._items.pop()
	
	def size(self):
		return len(self._items)
	
	
def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)
	
	while simqueue.size()>1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
		simqueue.dequeue()
	
	return simqueue.dequeue()
 

if __name__ == '__main__':
	# q = Queue()
	
	namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
	print(hotPotato(namelist, 7))