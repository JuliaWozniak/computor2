import re
from enum import Enum
import settings
from variable import Variable
from variable import Operation
from variable import OpList

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

def to_postfix(chunks):
	opstack = []
	converted = []
	start = True
	neg = False
	cur = Types_eq.NONE
	prev = Types_eq.NONE
	braces = 0
	opstr = settings.opstr + '('

	for c in chunks:
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
		if prev == cur and cur != Types_eq.PAR:
			print('successive elements')
			raise Exception('successive elements')
		prev = cur
		if braces < 0:
			print('some mamba-jamba with braces')
			raise Exception('unusual braces')
	if braces != 0:
		print('please close your braces')
		raise Exception('unusual braces')
	converted += opstack
	return(converted)

def postfix_to_vars(chunks):

	vars = OpList([])
	env = settings.env

	for c in chunks:
		is_var = re.match(r'(-)?[a-zA-Z]+', c)
		try:
			if is_var:
				vars.append(env.lookup(is_var.group(0)))
			elif c in opstr:
				vars.append(Operation(c))
			else:
				vars.append(Variable(c))
		except:
			print('ErrrOoOOR')
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
				res = op.op(a.value, b.value)
				rv = Variable(str(res))
				stack.insert(i, rv)
			i += 1
	if len(stack) == 1:
		res = stack.pop()
	else:
		print('why nothing?')
	if not isinstance(res, Variable):
		res = Variable(str(res))
	return (res)



def process_expression(s):
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





