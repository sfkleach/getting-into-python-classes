import math
import scipy.stats as stats

def distance(point2d):
    (x, y) = point2d
    return math.sqrt(x*x + y*y)

def angle(point2d):
    (x, y) = point2d
    return math.atan2(y, x)

def rotate(point2d, theta):
    (x, y) = point2d
    ct = math.cos(theta)
    st = math.sin(theta)
    return ct * x - st * y, st * x + ct * y

def midpoint(point2d):
    (x, y) = point2d
    return 0.5 * x, 0.5 * y

def probability(ndist, x):
    return stats.norm.cdf(x, ndist[0], ndist[1])

def variance(ndist):
    return ndist[1] * ndist[1]

def random(ndist):
    return stats.norm.rvs(loc=ndist[0], scale=ndist[1])

def midpoint(ndist):
    """This is a deliberate mistake illustrating when we have two functions with the same name."""
    return ndist[0]
