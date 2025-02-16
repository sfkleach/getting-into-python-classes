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
