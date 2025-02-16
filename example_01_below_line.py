
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
		return Point2D( ct * self.x - st * self.y, st * self.x + ct * self.y )

	def midpoint(self):
		return Point2D(0.5 * self.x, 0.5 * self.y)
	
class Line:

	def __init__(self, m, c):
		"""Describes the line y = mx + c"""
		self.m = m
		self.c = c

	def below_line(self, point2d: Point2D):
		"""Returns True if the point is below the line"""
		return point2d.y < self.m * point2d.x + self.c
