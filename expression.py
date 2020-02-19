import re
from enum import Enum
import settings
from variable import Variable
from variable import Operation
from variable import OpList
from postfix import to_postfix
from my_types import Imaginary

from enum import Enum


class Types(Enum):
	REAL = 1
	COMPLEX = 2
	MATRIX = 3
	NONE = 4
	OPERATION = 5


class Types_eq(Enum):
	PAR = 1
	OP = 2
	NUM = 3
	NONE = 4




def postfix_to_vars(chunks):

	vars = OpList([])
	env = settings.env
	opstr = settings.opstr

	for c in chunks:
		is_var = re.match(r'(-)?[a-zA-Z]+', c)
		try:
			if is_var:
				res = env.lookup(is_var.group(0))
				vars.append(res)
			elif c in opstr:
				vars.append(Operation(c))
			else:
				vars.append(Variable(c))
		except Exception as ax:
			print(ax)
	return (vars)

def evaluate_postfix(post):
	stack = post

	while len(stack) > 1:
		i = 0
		while i < len(stack):
			l = len(stack)
			if l == 1:
				return
			if isinstance(stack[i], Operation):
				op = stack.pop(i)
				b = stack.pop(i - 1)
				a = stack.pop(i - 2)
				i -= 2
				try:
					lt = a.type.value
					rt = b.type.value
					if (lt == Types.REAL.value and rt == Types.COMPLEX.value)\
					or (rt == Types.REAL.value and lt == Types.COMPLEX.value):
						if lt == Types.REAL.value:
							a.value = Imaginary(imaginary=0, real=a.value.a)
							a.type = Types.COMPLEX
						else:
							b.value = Imaginary(imaginary=0, real=b.value.a)
							b.type = Types.COMPLEX
					res = op.op(a, b)
					res.describe()
					res = Variable(res)

				except Exception as err:
					print(err)
					print('wrong with operation')
				stack.insert(i, res)
			i += 1
	if len(stack) == 1:
		res = stack.pop()
	else:
		print(len(stack))
		print('why nothing?')
	return (res)

def check_i(s):
	numeric_part = re.search(r'\d+', s.group(0))
	if numeric_part:
		return(numeric_part.group(0) + 'i')
	print('how to deal?')


def process_function(s, var_name):
	s = re.sub(r'\d+\*i', check_i, s)
	chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
	chunks = ' '.join(chunks).split()
	if chunks[0] == '-':
		if len(chunks) > 1 and re.match(r'\d+(\.\d+)?', chunks[1]):
			chunks[1] = '-' + chunks[1]
			chunks.pop(0)
	post = to_postfix(chunks)
	
	print(post)

def process_expression(s):
	s = re.sub(r'\d+\*i', check_i, s)
	chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
	chunks = ' '.join(chunks).split()
	if chunks[0] == '-':
		if len(chunks) > 1 and re.match(r'\d+(\.\d+)?', chunks[1]):
			chunks[1] = '-' + chunks[1]
			chunks.pop(0)
	post = to_postfix(chunks)
	print(post)
	varpost = postfix_to_vars(post)
	result = evaluate_postfix(varpost)
	return (result)





