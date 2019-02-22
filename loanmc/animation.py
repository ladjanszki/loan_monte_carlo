import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import optimize

import loanmc

 
def plot_yield_curves(data_df, params_df):
    data_group = data_df.groupby('Date')

    # The figure object
    fig, ax = plt.subplots()
    
    # All the plots
    ims = []
    
    # DataFrame to store the fit parameteres
    # params_df = pd.DataFrame(columns = ['Date', 'Beta1', 'Beta2', 'Beta3', 'Lambda', 'RSquared'])

    params_df = params_df.set_index('Date')
    
    for key, day in data_group:

        # Get yield cureve on a given day
        x_data = day['Year'].as_matrix() * 12
        y_data = day['Yield'].as_matrix()
        last_month = x_data.max()

        # Plot the original data 
        orig_data, = ax.plot(x_data, y_data, 'r-.', label='Actual data')

        title = ax.text(0.5,
                        1.05,
                        "Hungarian zero coupon yield at " + key, 
                        size=plt.rcParams["axes.titlesize"],
                        ha="center", 
                        transform=ax.transAxes, )
        
        beta1 = params_df.loc[key]['Beta1']
        beta2 = params_df.loc[key]['Beta2']
        beta3 = params_df.loc[key]['Beta3']
        lmbd = params_df.loc[key]['Lambda']

        ax.set(xlabel = 'Month')
        ax.set(ylabel = 'Yield [%]')

        t = np.linspace(0, last_month, 100)
        yc = loanmc.YieldCurve(beta1, beta2, beta3, lmbd)
        tmp2 = yc.calc(t)
        fitted, = ax.plot(t, tmp2, 'b-', label='Fitted')

        ax.legend()

        # Accumulate plots for animation
        ims.append([orig_data, fitted, title])
        

    # Creating an animation and save it
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=False, repeat_delay=1000)
    # ani.save('dynamic_images.mp4')
    plt.show()   
