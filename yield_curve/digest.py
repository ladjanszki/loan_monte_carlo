import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

# Getting the yiled curve data from file
df = pd.read_csv('2018.csv')

# Digest for our needs
# ['Unnamed: 0', 'Dátum/Date', 'Nap/Day', 'Év/Year', 'Hozam (%)/Yield (%)']
df = df.drop('Unnamed: 0', axis=1)
df.columns = ['Date', 'Day', 'Year', 'Yield']

# Get yield cureve on a given day
day = df[df['Date'] == '2018-12-03']
x_data = day['Year'].as_matrix()
x_data = x_data * 12
last_month = x_data.max()
y_data = day['Yield'].as_matrix()

# Plot it
plt.plot(x_data, y_data, 'r-.')

# Now fit a function to the data
def yield_curve(t, beta1, beta2, beta3, ldb):

    B1 = beta1
    B2 = beta2 * ((1 - np.exp(-ldb * t)) / (ldb * t))
    B3 = beta3 * (((1 - np.exp(-ldb * t)) / (ldb * t)) - np.exp(-ldb * t))

    return B1 + B2 + B3

# Fit the yield curve
params, params_covariance = optimize.curve_fit(yield_curve, x_data, y_data, p0=[0, 0.1, 0.1, 0.06])

b1 = params[0]
b2 = params[1]
b3 = params[2]
l = params[3]

print(params)

t = np.linspace(0, last_month, 100)
plt.plot(t, yield_curve(t, b1, b2, b3, l))
plt.show()
 
