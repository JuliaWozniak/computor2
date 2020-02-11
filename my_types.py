
class Real():

	def __init__(self, num):
		self.a = float(num)
		

	def describe(self):
		print(self.a)
	def __add__(self, o):
		if isinstance(o, Real):
			return self.a + o.a
		else:
			print("trying to add diff types")
	def __pow__(self, o):
		print("heeerrrreee")

