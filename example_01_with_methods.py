
import math

class Point2D:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

	def angle(self):
		return math.atan2(self.x, self.y)

	def rotate(self, theta):
		ct = math.cos(theta)
		st = math.sin(theta)
		return ct * self.x - st * self.y, st * self.x + ct * self.y

	def midpoint(self):
		return 0.5 * self.x, 0.5 * self.y
