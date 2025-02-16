import scipy.stats as stats

def probability(ndist, x):
    return stats.norm.cdf(x, ndist[0], ndist[1])

def variance(ndist):
    return ndist[1] * ndist[1]

def random(ndist):
    return stats.norm.rvs(loc=ndist[0], scale=ndist[1])

def midpoint(ndist):
    return ndist[0]
