<<<<<<< HEAD
def greeting(name: str) -> str:
    return 'Hello '


a = greeting(10)
=======
import re

def to_postfix(chunks):
	opstack = []
	converted = []
	start = True
	neg = False

	for c in chunks:
		# print(opstack)
		# print(converted)
		if c == ')':
			for i in reversed(opstack):
			 	if i == '(':
			 		start = True
			 		opstack.pop()
			 		pass
			 	else:
			 		converted.append(opstack.pop())
		elif c not in "(+-/*^":
			start = False
			if neg == True:
				c = '-' + c
			converted.append(c)
			# print('adding operand', c)
			neg = False
		else:
			if c == '(':
				start = True
			if start == True and c == '-':
				# print('HERE')
				neg = True
				c = ''
			else:
				opstack.append(c)
				# print('adding op', c)
	converted += opstack
	return(converted)

def process_expression(s):
	chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
	chunks = ' '.join(chunks).split()
	# if chunks[0] == '-':
	# 	if len(chunks) > 1 and re.match(r'\d+(\.\d+)?', chunks[1]):
	# 		chunks[1] = '-' + chunks[1]
	# 		chunks.pop(0)
	post = to_postfix(chunks)
	print(post)
	# varpost = postfix_to_vars(post)
	# result = evaluate_postfix(varpost)
	return (post)


# process_expression('9 + (-6 + 3)')

s = '5 + 8 - 7'
opstr = '+-/*^'

chunks = re.split(r'([\+\-\*\/\%\^\(\)\s])', s)
print(chunks)
chunks = re.split(r'(opstr)', s)

# process_expression('(-7 + 3)')

>>>>>>> 8f8e69fd6a309598ce0239f4c3ddc27cdffa4b3a
