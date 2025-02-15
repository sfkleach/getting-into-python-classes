
import math

def distance(x, y):
	'''Return the distance from the origin to the point (x, y).'''
	return math.sqrt(x*x + y*y)

def angle(x, y):
	'''Return the angle in radians between the positive x-axis and the point (x, y).'''
	return math.atan2(x, y)

def rotate(x, y, theta):
	'''Return the point (x, y) rotated by theta radians.'''
	ct = math.cos(theta)
	st = math.sin(theta)
	return ct * x - st * y, st * x + ct * y

def midpoint(x, y):
	'''Return the midpoint of the line segment from (0, 0) to (x, y).'''
	return 0.5 * x, 0.5 * y