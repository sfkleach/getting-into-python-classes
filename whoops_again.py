import math
import scipy.stats as stats

class NormalDistribution:

    def __init__(self, mean, stddev):
        self.mean = mean
        self.stddev = stddev

def probability(ndist, x):
    return stats.norm.cdf(x, ndist.mean, ndist.stddev)

def variance(ndist):
    return ndist.stddev * ndist.stddev

def random(ndist):
    return stats.norm.rvs(loc=ndist.mean, scale=ndist.stddev)

def midpoint(ndist):
    return ndist.mean

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

if __name__ == '__main__':
    print( midpoint( NormalDistribution(1, 0) ) )
    # Prints ... 
	# Traceback (most recent call last):
	#   File "/home/sfkleach/org/codehub/getting-into-python-classes/whoops_again.py", line 43, in <module>
	#     print( midpoint( NormalDistribution(1, 0) ) )
	#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	#   File "/home/sfkleach/org/codehub/getting-into-python-classes/whoops_again.py", line 40, in midpoint
	#     return 0.5 * p.x, 0.5 * p.y
	#                  ^^^
	# AttributeError: 'NormalDistribution' object has no attribute 'x'