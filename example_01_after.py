
import math

def distance(point2d):
	(x, y) = point2d
	return math.sqrt(x*x + y*y)

def angle(point2d):
	(x, y) = point2d
	return math.atan2(x, y)

def rotate(point2d, theta):
	(x, y) = point2d
	ct = math.cos(theta)
	st = math.sin(theta)
	return ct * x - st * y, st * x + ct * y

def midpoint(point2d):
	(x, y) = point2d
	return 0.5 * x, 0.5 * y
