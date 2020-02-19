from my_types import Real
from my_types import Imaginary
# from variable import Types

from enum import Enum

class Types(Enum):
	REAL = 1
	COMPLEX = 2
	MATRIX = 3
	NONE = 4
	OPERATION = 5



def multiply(left, right):
	lt = left.type
	rt = right.type
	if lt == rt:
		return(left.value * right.value)
	else:
		raise(Exception('different types, do not know yet'))

def adding(left, right):
	lt = left.type.value
	rt = right.type.value
	if lt == rt:
		return(left.value + right.value)
	else:
		raise(Exception('different types, do not know yet'))

def subtract(left, right):
	lt = left.type
	rt = right.type
	if lt == rt:
		return(left.value - right.value)
	else:
		raise(Exception('different types, do not know yet'))

def divide(left, right):
	lt = left.type
	rt = right.type
	if lt == rt:
		return(left.value / right.value)
	else:
		raise(Exception('different types, do not know yet'))

def modulo(left, right):

	lt = left.type.value
	rt = right.type.value
	if lt == Types.REAL.value and rt == Types.REAL.value:
		return left.value % right.value
	else:
		raise Exception('can only perform modulo operation on Rational numbers')



		