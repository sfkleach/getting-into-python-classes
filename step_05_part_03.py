
import math

class Point2D:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x
    
    def y(self):
        return self._y

    def distance(self):
        return math.sqrt(self._x * self._x + self._y * self._y)

    def angle(self):
        return math.atan2(self._y, self._x)

    def rotate(self, theta):
        ct = math.cos(theta)
        st = math.sin(theta)
        return Point2D(ct * self._x - st * self._y, st * self._x + ct * self._y)

    def midpoint(self):
        return Point2D(0.5 * self._x, 0.5 * self._y)


class PolarCoords:

    def __init__(self, r, theta):
        self._r = r
        self._theta = theta

    def x(self):
        return self._r * math.cos(self._theta)
    
    def y(self):
        return self._r * math.sin(self._theta)

    def distance(self):
        return self._r
    
    def angle(self):
        return self._theta

    def rotate(self, phi):
        return PolarCoords(self._r, self._theta + phi)

    def midpoint(self):
        return PolarCoords(0.5 * self._r, self._theta)
    

class Line:

    def __init__(self, m, c):
        """Describes the line y = mx + c"""
        self.m = m
        self.c = c

    def below_line(self, point2d: Point2D):
        """Returns True if the point is below the line"""
        return point2d.y() < self.m * point2d.x() + self.c
    

class NormalDistribution:
    """We can ignore this class for the remaining examples - included for completeness"""
    
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
