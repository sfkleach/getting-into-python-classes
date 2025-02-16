import math
import scipy.stats as stats

def probability(ndist, x):
    return stats.norm.cdf(x, ndist[0], ndist[1])

def variance(ndist):
    return ndist[1] * ndist[1]

def random(ndist):
    return stats.norm.rvs(loc=ndist[0], scale=ndist[1])

def midpoint(ndist):
    return ndist[0]

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

if __name__ == '__main__':
    print( probability(rotate((1, 0), math.pi/2), 1) )
    # Prints 0.8413447460685429 !