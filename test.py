import re
from abc import ABC, abstractmethod

class Operand(ABC):

	@abstractmethod
	def describe(self):
		pass
	@abstractmethod
	def __add__(self, other):
		pass
	# @abstractmethod
	# def __sub__(self, other):
	# 	pass
	# @abstractmethod
	# def __mul__(self, other):
	# 	pass
	# @abstractmethod
	# def __truediv__(self, other):
	# 	pass
	# @abstractmethod
	# def __mod__(self, other):
	# 	pass



class Real(Operand):

	def __init__(self, num):
		self.a = num
		

	def describe(self):
		print(self.a)
	def __add__(self, o):
		if isinstance(o, Real):
			return self.a + o.a
		else:
			print("trying to add diff types")
	def __pow__(self, o):
		print("heeerrrreee")



from enum import Enum
class Types(Enum):
	REAL = 1
	COMPLEX = 2
	MATRIX = 3
	NONE = 4

class Variable():

	def __init__(self, name, value, type=None):
		self.name = name
		self.value = value
		if isinstance(self.value, Real):
			self.type = Types.REAL
		else:
			self.type = Types.NONE
		
	def describe(self):
		self.value.describe()

class Operation():
	def __init__(self, sign):
		if sign == '+':
			self.op = add
			self.sign = sign
	def describe():
		print(self.sign)




def add(left, right):
	if left.type == Types.REAL and right.type == Types.REAL:
		return(left.value + right.value)
	else:
		print('different types, do not know yet')
		return(10)



a = Variable(' ', Real(6))
b = Variable(' ', Real(-10))

c = Variable(' ', Operation('+'))

print(c.value.op(a, b))
