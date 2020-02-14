from abc import ABC, abstractmethod
import re
from my_types import Real

class Op(ABC):

	@abstractmethod
	def describe(self):
		pass

##########
##########
##########

from collections import MutableSequence

class OpList(MutableSequence):
	def __init__(self, data=None):
	
		super(OpList, self).__init__()
		if (data is not None):
			self._list = list(data)
		else:
			self._list = list()
	def __repr__(self):
		return "<{0} {1}>".format(self.__class__.__name__, self._list)
	def __len__(self):
		return len(self._list)
	def __getitem__(self, ii):
		return self._list[ii]
	def __delitem__(self, ii):
		del self._list[ii]
	def __setitem__(self, ii, val):
		self._list[ii] = val
	def __str__(self):
		return str(self._list)
	def insert(self, ii, val):
		self._list.insert(ii, val)
	def append(self, val):
		self.insert(len(self._list), val)

##########
##########
##########


class Env():
	def __init__(self):
		self.my_vars = {}
		self.my_var_names = []

	def lookup(self, name):
		nameC = name.casefold()
		if nameC[0] == '-':
			print('need to negate a variable')
			nameC = nameC[1:]
		for c in self.my_var_names:
			if nameC == c.casefold():
				return(self.my_vars[c])
		raise Exception('no such variable')
	def assign(self, name, op):
		nameC = name.casefold()
		for c in self.my_var_names:
			if nameC == c.casefold():
				self.my_vars[c] = op
				return
		self.my_var_names.append(name)
		self.my_vars[name] = op
	def print_vars(self):
		for name in self.my_var_names:
			print("%s =" %(name), end=' ')
			self.my_vars[name].describe()



##########
##########
##########






from enum import Enum
class Types(Enum):
	REAL = 1
	COMPLEX = 2
	MATRIX = 3
	NONE = 4
	OPERATION = 5



##########
##########
##########




class Operation(Op):
	def __init__(self, sign):
		if sign == '+':
			self.op = add
		elif sign == '-':
			self.op = subtract
		else:
			raise Exception('unknown')
		self.sign = sign
	def describe(self):
		print(self.sign)

def get_type(value):
	is_rational = re.match(r'(-)?\d+(\.\d+)?', value)
	return(1, Real(float(is_rational.group(0))))



def add(left, right):
	lt = type(left)
	rt = type(right)
	if lt == rt:
		return(left + right)
	print('different types, do not know yet')
	return(10)

def subtract(left, right):
	lt = type(left)
	rt = type(right)
	if lt == rt:
		return(left - right)
	print('different types, do not know yet')
	return(10)
##########
##########
##########


class Variable(Op):

	def __init__(self, value, name='_'):
		self.name = name
		res, val = get_type(value)
		if res:
			self.value = val
		if isinstance(self.value, Real):
			self.type = Types.REAL
		else:
			raise Exception('unable to make a variable. unknown type')

	def describe(self):
		self.value.describe()

