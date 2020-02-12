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

def to_postfix(chunks):
	opstack = []
	converted = []

	for c in chunks:
		if c == ')':
			for i in reversed(opstack):
			 	if i == '(':
			 		opstack.pop()
			 		pass
			 	else:
			 		converted.append(opstack.pop())
		elif c not in "(+-/*^":
			converted.append(c)
		else:
			opstack.append(c)
	converted += opstack
	return(converted)

def postfix_to_vars(chunks):

	vars = OpList([])
	env = settings.env

	for c in chunks:
		is_var = re.match(r'[a-zA-Z]+', c)
		# maybe can just return from lookup if group == None
		if is_var:
			vars.append(env.lookup(is_var.group(0)))
			continue
		elif c in '+-/*^':
			vars.append(Operation(c))
			continue
		else:
			try:
			# try!!!!!
				vars.append(Variable(c))
			except:
				print('ErrrOoOOR')
	print('-------------------------------------------------')
	# for  v in vars:
	# 	v.describe()
	print('-------------------------------------------------')
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
		res = 10
	if not isinstance(res, Variable):
		res = Variable(str(res))
	return (res)



def process_expression(s):
	chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
	chunks = ' '.join(chunks).split()
	post = to_postfix(chunks)
	varpost = postfix_to_vars(post)
	result = evaluate_postfix(varpost)
	return (result)




class Types_eq(Enum):
	PAR = 1
	OP = 2
	NUM = 3
	NONE = 4

