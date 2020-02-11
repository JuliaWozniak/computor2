from abc import ABC, abstractmethod
import re

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

class Env():
	def __init__(self):
		self.my_vars = {}
		self.my_var_names = []

	def lookup(self, name):
		name = name.casefold()
		if name in self.my_var_names:
			return(self.my_vars[name])
		# raise an error
		print('no such variable')
		return('')
	def assign(self, name, op):
		name = name.casefold()
		if name in self.my_var_names:
			self.my_vars[name] = op
			return
		self.my_var_names.append(name)
		self.my_vars[name] = op
	def print_vars(self):
		for name in self.my_var_names:
			print("%s =" %(name), end=' ')
			self.my_vars[name].describe()

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

class Operation():
	def __init__(self, sign):
		if sign == '+':
			self.op = add
			self.sign = sign
	def describe():
		print(self.sign)



def add(left, right):
	if isinstance(left, Real) and isinstance(right, Real):
		return(left + right)
	else:
		print('different types, do not know yet')
		return(10)


from enum import Enum
class Types(Enum):
	REAL = 1
	COMPLEX = 2
	MATRIX = 3
	NONE = 4
	OPERATION = 5

class Variable():

	def __init__(self, name, value):
		self.name = name
		self.value = value
		if isinstance(self.value, Real):
			self.type = Types.REAL
		elif isinstance(self.value, Operation):
			self.type = Types.OPERATION
		else:
			self.type = Types.NONE

	def describe(self):
		print(self.type, end=' ')
		# self.value.describe()


