

def to_postfix(chunks):
	opstack = []
	converted = []
	i = 0
	print(chunks)
	for c in chunks:
		print(i, end=' ')
		print(opstack)
		print(converted)
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
		i +=1 
	converted += opstack
	print('postfix',converted)
	return(converted)


a = ['6', '+', '3']

b = to_postfix(a)


def evaluate_postfix(post):
	stack = post
	# i = 0

	while len(stack) > 1:
		i = 0
		print('how many times?')
		while i < len(stack):
			l = len(stack)
			if l == 1:
				print('wwww')
				return
			if stack[i] in '+*':
				o = stack.pop(i)
				b = stack.pop(i - 1)
				a = stack.pop(i - 2)
				i -= 2
				stack.insert(i, a + b)
			print(stack)
			i += 1


evaluate_postfix(b)


