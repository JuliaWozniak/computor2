import settings
import re
from enum import Enum
from variable import Variable
from variable import Real
from variable import Operation
from expression import process_expression
from expression import process_function
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
	is_func = re.match(r'func([a-zA-Z]+|(\d+(.\d+)?|))', s)
	if is_func:

		print('Fuuuunc')
		return(Type_LR.FNAME, 'x')
	try:
		s = s.strip()

		result_var = process_expression(s)
		print('wow')
		return(Type_LR.EXP, result_var)
	except:
		raise ValueError 

def right_when_variable(part, word):
	env = settings.env
	try:
		s = part.strip()
		result_var = process_expression(s)
	except Exception as ex:
		print('wrong with right side')
		print(ex)
	else:
		env.assign(word, result_var)
		return result_var

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
			final_result = right_when_variable(parts[1], word)
		elif left_res[0] == Type_LR.EXP:
			print('here we are')
			res = left_res[1]
			r = parts[1].strip()
			if r == '?':
				final_result = res
			else:
				raise Expression('wrong syntax')
		elif left_res[0] == Type_LR.FNAME:
			var_name = left_res[1]
			final_result = process_function(parts[1], var_name)
		else:
			print('why are we here?')
			final_result = None
			print('can\'t solve yet')
		print('#################')
		print('FINAL result is', final_result.value.describe())
		print('#################')
	except Exception as ax:
		print(ax)
		print('something wrong with left side')



