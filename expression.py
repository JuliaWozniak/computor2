import re
from enum import Enum
import settings
from second import Variable
from second import Real
from second import Operation

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
	if len(opstack) > 0:
		converted.append(opstack.pop())
	return(converted)

def postfix_to_vars(chunks):

	vars = []
	env = settings.env

	for c in chunks:
		is_var = re.match(r'[a-zA-Z]+', c)
		# maybe can just return from lookup if group == None
		if is_var:
			vars.append(env.lookup(is_var.group(0)))
			continue
		is_rational = re.match(r'(-)?\d+(\.\d+)?', c)
		if is_rational:
			# var = 
			vars.append(Variable(' ', Real(is_rational.group(0))))
			continue
		if c in '+-/*^':
			vars.append(Variable(' ', Operation(c)))
			continue
	i = 0
	while i < len(vars):
		vars[i].describe()
		i += 1

def perform_operation(a, b, op):



	if op == '+':
		print('add')
		return (a + b)
	elif op == '-':
		print('subtract')
		return (a - b)
	elif op == '*':
		print('multiply')
		return (a * b)
	elif op == '/':
		print('divide')
		return (a / b)

def evaluate_postfix(post):
	stack = []

	for p in post:
	# if binary operation
		if p in '+-/*^':
			b = stack.pop()
			res = perform_operation(stack.pop(), b, p)
			print(res)
			stack.append(res)
		else:
			stack.append(p)
	res = stack.pop()
	print(res)
	return (res)


def process_expression(s):
	chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
	chunks = ' '.join(chunks).split()
	post = to_postfix(chunks)
	
	varpost = postfix_to_vars(post)
	# result = evaluate_postfix(varpost)
	return chunks




class Types_eq(Enum):
	PAR = 1
	OP = 2
	NUM = 3
	NONE = 4

