class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		result = "Point(" + str(self.x) + ", " + str(self.y) + ")"
		return result

	def __add__(self, ponto):
		return Point(self.x + ponto.x, self.y+ponto.y)