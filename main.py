import re
import second
from second import Env
from second import Real




env = Env()

def process_computation(s):
	# while s:
	chunks = re.split(r'\s+', s)
	second_list = chunks.copy()
	for index, chunk in enumerate(chunks, start=0):
		if chunk in "+-*/%^()":
			continue
		res = re.match(r'\d+(\.\d+)?$', chunk)
		if res:
			continue
		mini_chunks = re.split(r'([\+\-\*\/\%\^\(\)])', chunk)
		if mini_chunks:
			mini_chunks = list(filter(None, mini_chunks))
			chunks.pop(index)
			for i in mini_chunks:
				chunks.insert(index, i)
				index += 1
	return chunks

from enum import Enum
class Types_eq(Enum):
	PAR = 1
	OP = 2
	NUM = 3
	NONE = 4


def check_computation(eq):
	prev = Types_eq.NONE
	cur = Types_eq.NONE

	stack = []
	for elem in eq:
		if elem in '/*+-%':
			cur = Types_eq.OP
			stack.append(elem)
			eq.remove(elem)
		e = re.match(r'\d+',elem)
		if e:
			cur = Types_eq.NUM
		if elem in '()':
			cur = Types_eq.PAR
			stack.append(elem)
			eq.remove(elem)
		if cur == prev:
			print('ERROR two equal parts successively')
			return -1
		prev = cur
	print(eq)
	print(stack)
	return (1)
# def turn_to_postfix(eq):
# 	stack = []
# 	i = 0
# 	prev = None
# 	l = eq.len()
# 	while i < l:

# 		i += 1



def process_right_side(s):

	print(s)
	s = s.strip()
	#  try rational
	match = re.match(r'(-)?\d+(\.\d+)?$', s)
	if match:
		it = re.search(r'(-)?\d+(\.\d+)?', s)
		a = float(it.group(0))
		r = Real(a)
		return(1, r)
	# matrices
	# complex
	#  try expression
	eq = process_computation(s)
	print(eq)
	res = check_computation(eq)
	if res != 1:
		print('errorsss')
		return (0, 0)

	return (0, 0)
	


def process_input(s):
	global env

	s = s.strip()
#
# if just variable name on the left
# 
	match = re.match(r'[a-zA-Z]+\s=', s)
	if match:
		word = s[match.start() : match.end() - 2]
		s = s[match.end():]

		(res, var) = process_right_side(s)

		if res:
			env.assign(word, var)
			print('new variable   %s' %(word))	


import sys

def main():
	global env
	while True:
		s = input('>  ')
		process_input(s)
		if s == 'stop':
			print('Finally')
			break
		if s == 'describe':
			env.print_vars()
	

if __name__ == '__main__':
	main()

