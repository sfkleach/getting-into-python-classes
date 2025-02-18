import math
import scipy.stats as stats


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def rotate(self, theta):
        ct = math.cos(theta)
        st = math.sin(theta)
        return Point2D(ct * self.x - st * self.y, st * self.x + ct * self.y)

    def midpoint(self):
        return Point2D(0.5 * self.x, 0.5 * self.y)


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
