#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Version: 0.1
# Author: Louis Lin <louislin15@yahoo.com>
# License: Copyright(c) 2019 Louis.Lin
# Summary: 
# Date: 2020/2/29 15:40

class Stack():
	def __init__(self):
		self._items = []
	
	def isEmpty(self):
		return self._items == []
	
	def push(self, item):
		self._items.append(item)
		
	def pop(self):
		return self._items.pop()
	
	def peek(self):
		return self._items[len(self._items) - 1]
	
	def size(self):
		return len(self._items)
	
#    栈的应用：括号匹配
def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol)
		elif symbol == ')':
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		
		index += 1
		
	if s.isEmpty() and balanced:
		return True
	else:
		return False
	
		
#    栈的应用：十进制转换为二进制
def divideBy2(decNumber):
	remstack = Stack()
	while decNumber>0:
		remstack.push(decNumber%2)
		decNumber = decNumber//2
		
	binString = ""
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())

	return binString
	
	
#    栈的应用：中缀表达式转换为后续表达式
#    例子：中缀表达式：A*B+C*D => 后缀表达式：AB*CD*+
def infixToPostfix(infixexpr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opstack = Stack()
	postfixList = []
	tokenList = infixexpr.split()
	
	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opstack.push(token)
		elif token == ')':
			topToken = opstack.pop()
			while topToken != "(":
				postfixList.append(topToken)
				topToken = opstack.pop()
		else:
			while (not opstack.isEmpty()) and prec[opstack.peek()] >= prec[token]:
				postfixList.append(opstack.pop())
			opstack.push(token)
			
	while not opstack.isEmpty():
		postfixList.append(opstack.pop())
	
	return " ".join(postfixList)


#    栈的应用：后缀表达式计算
def postfixEval(postfixExpr):
	operandStack = Stack()
	tokenList = postfixExpr.split()
	for token in tokenList:
		if token in "0123456789":
			operandStack.push(int(token))
		else:
			opera1 = operandStack.pop()
			opera2 = operandStack.pop()
			result = doMath(token, opera1, opera2)
			operandStack.push(result)
	
	return operandStack.pop()

def doMath(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2
	
	
	
if __name__ == '__main__':
	# stack类测试
	print("new stack")
	s = Stack()
	print("check is empty ", s.isEmpty())
	print("stack length : ", s.size())
	print("stack push 2")
	s.push(2)
	print("stack push dog")
	s.push('dog')
	print("check is empty ", s.isEmpty())
	print("stack length : ", s.size())
	print("stack top : ",s.peek())
	print("stack pop ", s.pop())
	print("check is empty ", s.isEmpty())
	print("stack top : ", s.peek())
	
	#栈应用之括号匹配规则
	print("'((()))' ", parChecker('((()))'))
	print("'((())' ", parChecker('((()))'))
	
	print(divideBy2(12))
	print(divideBy2(233))
	
	print("中缀表达式：A*B+C*D")
	print(infixToPostfix("A * B + C * D"))
	
	print("后缀表达式：4 5 6 * +")
	print(postfixEval("4 5 6 * +"))
 
 
 

