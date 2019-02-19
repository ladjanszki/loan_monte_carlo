import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import optimize

import loanmc
 
def plot_yield_curves(data_df, params_df):
    data_group = data_df.groupby('Date')
    #params_group = data_df.groupby('Date')

    # The figure object
    fig = plt.figure()
    
    # All the plots
    ims = []
    
    # DataFrame to store the fit parameteres
    # params_df = pd.DataFrame(columns = ['Date', 'Beta1', 'Beta2', 'Beta3', 'Lambda', 'RSquared'])
    
    for key, day in data_group:

        # Get yield cureve on a given day
        x_data = day['Year'].as_matrix() * 12
        y_data = day['Yield'].as_matrix()
        last_month = x_data.max()

        # Adding title to the animation
        # plt.title(key)
        
        # Plot the original data 
        orig_data, = plt.plot(x_data, y_data, 'r-.')
        
        # Plot the fitted data
        # TODO: This is UGLY for the vectorzied function numpy vectorize have to be explicitly called
        #       Vectorization have to be done in the class definition
        params = params_df.loc[params_df['Date'] == key]
        t = np.linspace(0, last_month, 100)
        yc = loanmc.YieldCurve(params['Beta1'], params['Beta2'], params['Beta3'], params['Lambda'])
        func = np.vectorize(yc.calc)
        fitted, = plt.plot(t, func(t), 'b-')
        
        # Accumulate plots for animation
        ims.append([orig_data, fitted])
        
        
    # Creating an animation and save it
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
    # ani.save('dynamic_images.mp4')
    plt.show()   
