from abc import ABC, abstractmethod
import math
import re

class Var(ABC):
	@abstractmethod
	def __add__(self):
		pass
	@abstractmethod
	def __sub__(self):
		pass
	# @abstractmethod
	# def negate(self):
	# 	pass





class Imaginary(Var):

	def __init__(self, imaginary, real=0):
		if (isinstance(imaginary, str)):
			ir = re.match(r'\d+(.\d+)?', imaginary)
			self.i = float(ir.group(0))
		else:
			self.i = imaginary
		self.r = real

	def describe(self):
		print('%.2f + %.2fi' %(self.r, self.i))
	def __add__(self, o):
		r = Imaginary(imaginary=(self.i + o.i), real = (self.r + o.r))
		return r
	def __sub__(self, o):
		r = Imaginary(imaginary=(self.i - o.i), real = (self.r - o.r))
		return r
	def __mul__(self, o):
		with_i = (self.r * o.i) + (self.i * o.r)
		without_i = (self.r * o.r) - (self.i * o.i)
		r = Imaginary(imaginary=with_i, real=without_i)
		return r

class Real(Var):

	def __init__(self, num):

		self.a = float(num)
		

	def describe(self):
		print(self.a)
	def __add__(self, o):
		r = Real(self.a + o.a)
		return r
	def __sub__(self, o):
		r = Real(self.a - o.a)
		return r
	def __truediv__(self, o):
		r = Real(self.a / o.a)
		return r
	def __mul__(self, o):
		r = Real(self.a * o.a)
		return r
	def __mod__(self, o):
		r = Real(self.a % o.a)
		return r
	def negate(self):
		print('negaaaatingggg')
		self.a = -(self.a)
		print('result of negation', res)
		return self


