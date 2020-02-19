from enum import Enum
from variable import OpList


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
	opstr = '+-/*^(%'

	for c in chunks:
		if c == ')':
			braces -= 1
			cur = Types_eq.PAR
			for i in reversed(opstack):
			 	if i == '(':
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
					if pr in '*/%':
						pr = 1
					elif pr == '(':
						prev = cur
						continue
					else:
						pr = 0
					if cr in '*/%':
						cr = 1
					elif cr == '(':
						cr = 2
					else:
						cr = 0
					if cr <= pr:
						converted += opstack.pop(-2)
						if len(opstack) > 1 and opstack[-2] != '(':
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
