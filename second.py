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
	def assign(self, name, op):
		for n in self.my_var_names:
			if name.casefold() == n.casefold():
				self.my_vars[n] = op
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


