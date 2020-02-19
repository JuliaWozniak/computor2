from abc import ABC, abstractmethod
import re
from my_types import Real
from my_types import Imaginary
from operations import adding
from operations import subtract
from operations import multiply
from operations import divide
from operations import modulo


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
		neg = 0
		if nameC[0] == '-':
			nameC = nameC[1:]
			neg = 1
		for c in self.my_var_names:
			if nameC == c.casefold():
				if neg:
					print(self.my_vars[c])
					res = self.my_vars[c].negate()
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
			self.op = adding
		elif sign == '-':
			self.op = subtract
		elif sign == '^':
			self.op = power
		elif sign == '/':
			self.op = divide
		elif sign == '*':
			self.op = multiply
		elif sign == '%':
			self.op = modulo
		else:
			raise Exception('unknown')
		self.sign = sign

	def describe(self):
		print(self.sign)


def get_type(value):
	is_rational = re.match(r'(-)?\d+(\.\d+)?$', value)
	if is_rational:
		return(Real(float(is_rational.group(0))), Types.REAL)
	is_imaginary = re.match(r'(-)?\d+(\.\d+)?(\*i|i)', value)
	if is_imaginary:
		res = Imaginary(is_imaginary.group(0))
		return(res, Types.COMPLEX)

	raise Exception('unknown type')

def power(left, right):
	if isinstance(left, Real) and isinstance(right, Real):
		return(math.pow(left, right))
	if isinstance(right, Comple):
		raise(Exception('can not raise to complex power'))
	
	else:
		raise(Exception('different types, do not know yet'))




##########
##########
##########

class Variable(Op):

	def __init__(self, value, name='_'):
		self.name = name
		try:
			if isinstance(value, str):
				(val, t) = get_type(value)
			else:
				val = value
				if isinstance(value, Real):
					t = Types.REAL
				elif isinstance(value, Imaginary):
					t = Types.COMPLEX
				else:
					t = Types.NONE
		except Exception as ax:
			print(ax)
			raise Exception('unable to make a variable. unknown type')
		else:
			self.value = val
			self.type = t	

	def describe(self):
		self.value.describe()

	def negate(self):
		self.value = self.value.negate()
		return(self.value)


		
