import settings
import re
from enum import Enum
from variable import Variable
from variable import Real
from variable import Operation
from expression import process_expression

def process_right_side(s):
	s = s.strip()
	res = process_expression(s)
	return (1, res)
	

class Type_LR(Enum):
	VAR = 1
	FNAME = 2
	FIMG = 3
	EXP = 4
	NONE = 5
 
def process_left_side(s):
	s = s.strip()
	# if just variable name on the left
	match = re.match(r'[a-zA-Z]+$', s)
	if match:
		word = s[match.start() : match.end()]
		s = s[match.end():]
		return (Type_LR.VAR, word)

	return(Type_Lft.NONE, None)

def right_when_variable(part, word):
	env = settings.env
	(res, var) = process_right_side(part)
	if res:
		env.assign(word, var)
		print('new variable   %s' %(word))


def process_input(s):
	env = settings.env

	s = s.strip()
	parts = s.split('=')
	if len(parts) != 2:
		print('Syntax error with \'=\'')
		return()

	left_res = process_left_side(parts[0])
	if left_res[0] == Type_LR.VAR:
		word = left_res[1]
		right_when_variable(parts[1], word)
	else:
		print('can\'t solve yet')


