import numpy as np


class YieldCurve(object):
    """
    This functor servers as a paramteric yield curve

    Our assumption here is that the beta parameters
    and the time given for the calc method are compatible.
    (e.g. if the beta parameters were fitted for months
    the time have to be gicen in months)
    """

    def __init__(self, beta1, beta2, beta3, ldb):
        self.beta1 = beta1
        self.beta2 = beta2
        self.beta3 = beta3
        self.ldb = ldb

    def calc(self, t):

        B1 = self.beta1
        B2 = self.beta2 * ((1 - np.exp(-self.ldb * t)) / (self.ldb * t))
        B3 = self.beta3 * (((1 - np.exp(-self.ldb * t)) / (self.ldb * t)) - np.exp(-self.ldb * t))

        return B1 + B2 + B3

    def fit(self, t, beta1, beta2, beta3, ldb):
        self.beta1 = beta1
        self.beta2 = beta2
        self.beta3 = beta3
        self.ldb = ldb

        return self.calc(t)

