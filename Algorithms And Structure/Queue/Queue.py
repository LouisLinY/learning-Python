#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/3/1 21:23
import random


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


class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm         #打印速度
		self.currentTask = None     #打印任务
		self.timeRemaining = 0      #任务倒计时
	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			if self.timeRemaining <= 0:
				self.currentTask = None
	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False
	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task:
	def __init__(self, time):
		self.timestamp = time                       #生成时间戳
		self.pages = random.randrange(1, 21)        #打印页数
	def getStamp(self):
		return self.timestamp
	def getPages(self):
		return self.pages
	def waitTime(self, currenttime):
		return currenttime- self.timestamp          #等待时间

def newPrintTask():
	num = random.randrange(1, 181)                  #1/180概率生成作业
	if num == 180:
		return True
	else:
		return False

def simulation(numSeconds, pagesPerMinute):
	labprinter = Printer(pagesPerMinute)
	printQueue = Queue()
	waitingtimes = []
	for currentSecond in range(numSeconds):
		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)
		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)
		labprinter.tick()
	averageWait = sum(waitingtimes)/len(waitingtimes)
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size()))



if __name__ == '__main__':
	# q = Queue()
	
	namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
	print(hotPotato(namelist, 7))
	# 打印任务问题：运行和分析
	#按5PPM、1个小时的设定，模拟运行10次
	#总平均等待时间93.1秒，最长的平均等待时间164秒，最短的平均等待时间26秒
	#模拟3次，还有作业没有开始打印
	for i in range(10):
		simulation(3600, 5)