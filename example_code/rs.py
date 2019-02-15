import random 
import matplotlib.pyplot as plt
import scipy.special
from math import pow
import numpy as np


def pdf(x, alpha, beta):
    '''
    This is a probaility distribution function of 
    an artificial distribution we have prom previous measurements for example

    Actually this is a beta distribution
    '''

    B = scipy.special.gamma(alpha)*scipy.special.gamma(beta) / scipy.special.gamma(alpha + beta)

    pdf_beta = pow(x, alpha-1)*pow(1-x, beta - 1) / B
  
    return pdf_beta

# Generate values from the Beta distribution
NPOINTS = 1000
alpha = 2
beta = 5

x = []
y = []
for i in range(NPOINTS):
    x_val = i / NPOINTS
    x.append(x_val)
    y.append(pdf(x_val, alpha, beta))

# Reject sampling algorithm

# Get maximum of the distribution for enveloping
M = max(y)
print(M)

random.seed(1011)
values = []
N_SAMPLE = 100
for i in range(N_SAMPLE):
    ux = random.uniform(0, 1)
    uy = random.uniform(0, M + 1)


    if uy <= pdf(ux, alpha, beta):

        print(ux, uy)
        values.append(ux)

# Normalize to get a discrete pdf
hist, bins = np.histogram(values)
valid_points = len(values)
print('Valid points: ' + str(valid_points))
print('Sample points: ' + str(N_SAMPLE))

hist = hist / valid_points
print(hist.sum())
bins = np.delete(bins, -1)
#print(len(hist))
#print(len(bins))
#
#print(type(hist))
#print(type(bins))

# Plotting the results


plt.bar(bins, hist, width=0.01)
plt.plot(x, y, 'r')
plt.show()
    


