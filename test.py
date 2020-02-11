from collections.abc import MutableSequence
from abc import ABC, abstractmethod





class Op(ABC):

	@abstractmethod
	def describe(self):
		pass


class Operation(Op):
	def __init__(self, sign):
		if sign == '+':
			self.op = add
			self.sign = sign
	def describe():
		print(self.sign)



def add(left, right):
	if isinstance(left, Real) and isinstance(right, Real):
		return(left + right)
	else:
		print('different types, do not know yet')
		return(10)



if __name__=='__main__':
    foo = OpList([])
    a = Operation('+')
    foo.append(a)
    print (foo)  # <MyList [1, 2, 3, 4, 5, 6]>