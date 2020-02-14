import settings
import re
from enum import Enum
from variable import Variable
from variable import Real
from variable import Operation
from expression import process_expression

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


	raise ValueError 

def right_when_variable(part, word):
	env = settings.env
	try:
		s = part.strip()
		result_var = process_expression(s)
	except Exception as ex:
		print('wrong with right side')
		print(ex)
	except:
		print('something else wrong with right side')
	else:
		env.assign(word, result_var)
		print(result_var.describe())

def process_input(s):
	env = settings.env

	s = s.strip()
	parts = s.split('=')
	if len(parts) != 2:
		print('Syntax error with \'=\'')
		return()
	try:
		left_res = process_left_side(parts[0])
		if left_res[0] == Type_LR.VAR:
			word = left_res[1]
			right_when_variable(parts[1], word)
		else:
			print('can\'t solve yet')
	except:
		print('something wrong with left side')



