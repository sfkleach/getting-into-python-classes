import scipy.stats as stats
import math

class NormalDistribution:

    def __init__(self, mean, stddev):
        self.mean = mean
        self.stddev = stddev

    def probability(self, x):
        return stats.norm.cdf(x, self.mean, self.stddev)

    def variance(self):
        return self.stddev * self.stddev

    def random(self):
        return stats.norm.rvs(loc=self.mean, scale=self.stddev)

    def midpoint(self):
        return self.mean

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
		return Point2D(ct * self.x - st * self.y, st * self.x + ct * self.y)

	def midpoint(self):
		return Point2D(0.5 * self.x, 0.5 * self.y)

if __name__ == '__main__':
    print( NormalDistribution(1, 0).midpoint() )
    print( Point2D(1, 0).midpoint() )
    # Prints 1 and then (0.5, 0.0)
