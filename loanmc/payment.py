from scipy.optimize import newton
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# from yield_curve import YieldCurve


class Payment(object):

    def __init__(self, H, T, yc):
        self.H = H #Total value of loan
        self.T = T #Payment time (Should be given in months)
        self.yc = yc #Yield curve object
        self.exc = 0.0

    def set_exc(self, exc):
        self.exc = exc

    def calc_payment(self):
        
        #if not abs(remaining(C_res, H, T, r)) < 10e-8:
        #    print("nem konvergalt")
        #

        # A torleszto kiszamolasa solverrel
        return newton(self.remaining, 10000)

    def remaining(self, c):

        rem = self.H

        for t in range(1, self.T):
            k = (self.yc.calc(t) / 100) + self.exc  # Kamat amit a bank ker
            rem = float(rem) * float((1 + k)) - c
           

        return rem
 
