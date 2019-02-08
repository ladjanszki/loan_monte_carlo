import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import optimize

# Seeding the random generator
np.random.seed(21343356)

# Yield curve function form
def yield_curve(t, beta1, beta2, beta3, ldb):

    B1 = beta1
    B2 = beta2 * ((1 - np.exp(-ldb * t)) / (ldb * t))
    B3 = beta3 * (((1 - np.exp(-ldb * t)) / (ldb * t)) - np.exp(-ldb * t))

    return B1 + B2 + B3

# Getting the yiled data from file
df = pd.read_csv('2018.csv')

# Digest for our needs
# ['Unnamed: 0', 'Dátum/Date', 'Nap/Day', 'Év/Year', 'Hozam (%)/Yield (%)']
df = df.drop('Unnamed: 0', axis=1)
df.columns = ['Date', 'Day', 'Year', 'Yield']

grouped = df.groupby('Date')

# The figure object
fig = plt.figure()

# All the plots
ims = []

# DataFrame to store the fit parameteres
params_df = pd.DataFrame(columns = ['Date', 'Beta1', 'Beta2', 'Beta3', 'Lambda', 'RSquared'])

for key, day in grouped:

    # Get yield cureve on a given day
    #day = df[df['Date'] == '2018-12-03']
    x_data = day['Year'].as_matrix()
    x_data = x_data * 12
    last_month = x_data.max()
    y_data = day['Yield'].as_matrix()
    
    while True:

        # Initial parameters for the fit
        #init_params = [0, 0.1, 0.1, 0.06]
        init_params = np.random.rand(4)

        # Fit the yield curve
        params, params_covariance = optimize.curve_fit(yield_curve, x_data, y_data, p0=init_params)

        # TODO: 
        # This decomposition should be avioded by having one list argument 
        # for the paramteres in yield_curve function
        b1 = params[0]
        b2 = params[1]
        b3 = params[2]
        l = params[3]

        # Get the R squared of the fit
        #opt, pcov = curve_fit(f, xdata, ydata)
        residuals = y_data - yield_curve(x_data, b1, b2, b3, l)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((y_data-np.mean(y_data))**2)
        r_squared = 1 - (ss_res / ss_tot)

        # Guessing the next fit with the converged values
        # This is not a good idea since it restricts the optimization space
        # NOTE: Sometimes this rigidity is not so beneficial
        #init_params = params

        if(r_squared > 0.99):
            print(r_squared)
            break
   

    # Plot the original data 
    orig_data, = plt.plot(x_data, y_data, 'r-.')
    
    # Plot the fitted data
    t = np.linspace(0, last_month, 100)
    fitted, = plt.plot(t, yield_curve(t, b1, b2, b3, l), 'b-')

    # Accumulate plots for animation
    ims.append([orig_data, fitted])

    row = {'Date'   : key, 
           'Beta1'  : b1,
           'Beta2'  : b2,
           'Beta3'  : b3,
           'Lambda' : l,
           'RSquared': r_squared 
    }

    params_df = params_df.append(row, ignore_index=True)
 


#ims = []
#for i in range(60):
#
#    line, = plt.plot(float(i/10), float(i/10), 'ro')
#    ims.append([line])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

#ani.save('dynamic_images.mp4')
plt.show()


print(params_df.head())
 





 
