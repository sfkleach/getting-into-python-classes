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
    
    def distance_between(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx * dx + dy * dy)

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
    
    def distance_between(self, other):
        r2self = self._r * self._r
        r2other = other._r * other._r
        cdelta = math.cos(self._theta - other._theta)
        return math.sqrt(r2self + r2other - 2 * self._r * other._r * cdelta)
    
class Line:

    def __init__(self, m, c):
        """Describes the line y = mx + c"""
        self._m = m
        self._c = c

    def below_line(self, point2d: Point2D):
        """Returns True if the point is below the line"""
        return point2d.y() < self._m * point2d.x() + self._c

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
