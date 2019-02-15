import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import truncnorm
 
#Domain of X
xdomain = [-3, 3]
 
#Multiplier Constant
M = 2.0
 
def pdf(x):
    """
    Probability distribution function for Random Variable X
    from which we want to sample points. Here we assume
    we have truncated standard normal distribution in the domain of -3 to 3
    """
    return truncnorm.pdf(x, xdomain[0], xdomain[1])
 
def random_point_within_enveloping_region():
    """
    Return random point within the enveloping region.
    For x we will randomly sample point between -3 and 3
    Since we are assuming uniform distribution, the height of the enveloping region
    at any x is 1/6. So for Y we randomly sample point between 0 and 1/6
    """
    #Randomly sample x from -3 to 3
    x = random.uniform(xdomain[0], xdomain[1])
 
    # probability of obtain any x is equal to 1/6. i.e. height of enveloping region
    # for any X is 1/6.
    y = random.uniform(0, M * 1.0/6.0 )
 
    return (x,y)
 
def height_of_enveloping_region(x):
    """Return height of enveloping region at x."""
    return M * 1.0/6.0
 
#Number of sample points to sample
n = 10000
 
#Creating two arrays to capture accepted and rejected points
accepted = []
rejected = []
M = 2.0
 
#Run this loop until we got required number of valid points
while len(accepted) < n:
 
    #Get random point
    x, y = random_point_within_enveloping_region()
 
    #If for any x if envelping region is below the distribution from which we want to sample points
    #increment the multipler constant and resample all the points.
    if height_of_enveloping_region(x) < pdf(x):
        print("Increasing M from {0} to {1}".format(M, M+1))
        accepted = []
        rejected = []
        M += 1.0
        continue
 
    #If y is below blue curve then accept it
    if y < pdf(x):
        accepted.append((x, y))
    #otherwise reject it.
    else:
        rejected.append((x, y))

# Create histogram from accepted values
tmp = []
for pair in accepted:
    tmp.append(pair[0])

hist, bins = np.histogram(tmp)

print(hist)
print(hist.sum())
print(bins) 
midpoints = bins[:-1] + np.diff(bins) / 2

dens = hist / hist.sum() #* M

 
x = np.linspace(-3, 3, 100)
plt.plot(x, [pdf(i) for i in x], color='blue')
plt.bar(midpoints, dens, width = 0.05)
#plt.plot(x, [1.0/6 for i in x], color='black', ls='dashed', lw=1)
#plt.plot(x, [M * 1.0/6 for i in x], color='black', ls='dashed', lw=2)
#plt.plot([x[0] for x in accepted], [x[1] for x in accepted] , 'ro', color='g')
#plt.plot([x[0] for x in rejected], [x[1] for x in rejected] , 'ro', color='r')
plt.show()
 
##Calculate expected value for the truncated standard normal distribution
#approxMean = sum([x[0] for x in accepted])/len(accepted)
#print "Expected Mean = ", 0, pdf(0)
#print "Approximated Mean = ", approxMean, pdf(approxMean)
#print "Approximated Variance = ", sum([(x[0] - approxMean)**2 for x in accepted])/(len(accepted)-1)

