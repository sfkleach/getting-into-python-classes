import scipy.stats as stats

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
