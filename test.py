<<<<<<< HEAD
def greeting(name: str) -> str:
    return 'Hello '


a = greeting(10)
=======
import re

from collections.abc import MutableSequence

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

from enum import Enum


class Types_eq(Enum):
	PAR = 1
	OP = 2
	NUM = 3

	NONE = 4


def to_postfix(chunks):
	opstack = []
	converted = []
	start = True
	neg = False
	cur = Types_eq.NONE
	prev = Types_eq.NONE
	braces = 0
	opstr = '+-/*^' + '('

	for c in chunks:
		print(converted)
		print(opstack)
		if c == ')':
			braces -= 1
			cur = Types_eq.PAR
			for i in reversed(opstack):
			 	if i == '(':
			 		start = True
			 		opstack.pop()
			 		pass
			 	else:
			 		converted.append(opstack.pop())
		elif c not in opstr:
			cur = Types_eq.NUM
			start = False
			if neg == True:
				c = '-' + c
			converted.append(c)
			neg = False

		else:
			if c == '(':
				braces += 1
				cur = Types_eq.PAR
				start = True
			else:
				cur = Types_eq.OP
			if start == True and c == '-':
				neg = True
				c = ''
			else:
				opstack.append(c)
				if len(opstack) > 1:
					pr = opstack[-2]
					cr = opstack[-1]
					if pr in '*/':
						pr = 1
					elif pr == '(':
						prev = cur
						continue
					else:
						pr = 0
					if cr in '*/':
						cr = 1
					elif cr == '(':
						cr = 2
					else:
						cr = 0
					if cr <= pr:
						converted += opstack.pop(-2)
						if len(opstack) > 1:
							converted += opstack.pop(-2)
		if prev == cur and cur != Types_eq.PAR:
			raise Exception('successive elements')
		prev = cur
		if braces < 0:
			raise Exception('some mamba-jamba with braces')
	if braces != 0:
		raise Exception('please close your braces')
	while (len(opstack) > 0):
		converted += opstack.pop()
	return(converted)



def process_expression(s):
	# s = re.sub(r'\d+\*i', check_i, s)
	chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
	chunks = ' '.join(chunks).split()
	if chunks[0] == '-':
		if len(chunks) > 1 and re.match(r'\d+(\.\d+)?', chunks[1]):
			chunks[1] = '-' + chunks[1]
			chunks.pop(0)
	post = to_postfix(chunks)
	print(post)



process_expression('5 + 3 * (6 + 4) + 7 / 4')


>>>>>>> 8f8e69fd6a309598ce0239f4c3ddc27cdffa4b3a
