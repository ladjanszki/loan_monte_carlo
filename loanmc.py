import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import optimize

import loanmc

# Loading data into DataHandler
dh = loanmc.DataHandler()
dh.import_xls('./historical_data/ZERO_2018.xlsx')
dh.import_xls('./historical_data/ZERO_2017.xlsx')
# dh.stats()
# dh.to_csv('./historical_data/ZERO.csv')

# Truncate a few values for testing
tmp = dh.df.head()

# Fitting the model for all row
params_df = loanmc.fit_yield_curves(tmp)

#print(params_df)

exit(0)
# Testing YieldCurve class
yc = loanmc.YieldCurve(1, 2, 3, 0.1)
print(yc.calc(4))
print(yc.fit(4, 1, 2, 3, 0.1))
print(yc.fit(4, 2, 2, 2, 0.1))


def plot_yield_curves(data_df, params_df):
    grouped = data_df.groupby('Date')

    # The figure object
    fig = plt.figure()
    
    # All the plots
    ims = []
    
    # DataFrame to store the fit parameteres
    params_df = pd.DataFrame(columns = ['Date', 'Beta1', 'Beta2', 'Beta3', 'Lambda', 'RSquared'])
    
    for key, day in grouped:
        
        
        
    # The figure object
    fig = plt.figure()
    
    # All the plots
    ims = []
    
    # Plot the original data 
    orig_data, = plt.plot(x_data, y_data, 'r-.')
    
    # Plot the fitted data
    t = np.linspace(0, last_month, 100)
    fitted, = plt.plot(t, yield_curve(t, b1, b2, b3, l), 'b-')
    
    # Accumulate plots for animation
    ims.append([orig_data, fitted])
    
    
    # Creating an animation and save it
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
    # ani.save('dynamic_images.mp4')
    plt.show()
