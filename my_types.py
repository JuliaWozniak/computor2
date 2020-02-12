
class Real():

	def __init__(self, num):
		self.a = float(num)
		

	def describe(self):
		print(self.a)
	def __add__(self, o):
		return self.a + o.a
	def __sub__(self, o):
		return self.a - o.a
	def __pow__(self, o):
		print("heeerrrreee")

