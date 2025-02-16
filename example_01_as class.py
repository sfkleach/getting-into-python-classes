
import math

class Point2D:

	def __init__(self, x, y):
		self.x = x
		self.y = y

def distance(p):
	return math.sqrt(p.x*p.x + p.y*p.y)

def angle(p):
	return math.atan2(p.x, p.y)

def rotate(p, theta):
	ct = math.cos(theta)
	st = math.sin(theta)
	return ct * p.x - st * p.y, st * p.x + ct * p.y

def midpoint(p):
	return 0.5 * p.x, 0.5 * p.y
