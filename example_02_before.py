import scipy.stats as stats

def probability(mean, stddev, x):
    return stats.norm.cdf(x, mean, stddev)

def variance(stddev):
    return stddev * stddev

def random(mean, stddev):
    return stats.norm.rvs(loc=mean, scale=stddev)

def midpoint(mean, stddev):
    return mean
