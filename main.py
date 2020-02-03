from abc import ABC, abstractmethod
import re
import keyboard



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

	def __init__(self, a):
		self.a = a
	def describe(self):
		print(self.a)
	def __add__(self, o):
		return self.a + o.a
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

my_vars = {}
my_var_names = []




def deal_with_variables(word, str):
	global my_vars
	global my_var_names

	if word in my_var_names:
		print('reassigning variable')
	else:
		my_vars[word] = Variable(word, "value")
		my_var_names.append(word)
	print(my_var_names)
	print("wut")

def process_input(s):
	
	s = s.strip()

	match = re.match(r'[a-zA-Z]+\s=', s)
	if match:
		word = s[match.start() : match.end() - 2]
		s = s[match.end():]
		deal_with_variables(word, s)
		print('new variable   %s' %(word))



import sys
import keyboard

def main():
	while True:
		s = input('>  ')
		process_input(s)
		if s == 'stop':
			print('Finally')
			break
	

	# print(s)
if __name__ == '__main__':
	main()

