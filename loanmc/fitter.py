import numpy as np
import pandas as pd
from scipy import optimize
from loanmc import YieldCurve as yc


def fit_yield_curves(df):

    # Seeding the random generator
    np.random.seed(21343356)

    # Grouping the yield curve data
    # Every day is a different group
    grouped = df.groupby('Date')

    # DataFrame to store the fit parameteres
    params_df = pd.DataFrame(columns = ['Date', 'Beta1', 'Beta2', 'Beta3', 'Lambda', 'RSquared'])

    for key, day in grouped:
        
        # Get yield cureve on a given day
        x_data = day['Year'].as_matrix() * 12
        y_data = day['Yield'].as_matrix()

        # Loop to try several models for a curve
        while True:

            init_params = np.random.rand(4)

            # Fit the yield curve
            current_yc = yc(init_params[0], init_params[1], init_params[2], init_params[3])
            #params, params_covariance = optimize.curve_fit(yield_curve, x_data, y_data, p0=init_params)
            params, params_covariance = optimize.curve_fit(current_yc.fit, x_data, y_data, p0=init_params)

            # TODO: 
            # This decomposition should be avioded by having one list argument 
            # for the paramteres in yield_curve function
            #b1 = params[0]
            #b2 = params[1]
            #b3 = params[2]
            #l = params[3]

            # Get the R squared of the fit
            #opt, pcov = curve_fit(f, xdata, ydata)
            #residuals = y_data - yield_curve(x_data, b1, b2, b3, l)
            residuals = y_data - current_yc.calc(x_data)
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

        row = {'Date': key,
               'Beta1': current_yc.beta1,
               'Beta2': current_yc.beta2,
               'Beta3': current_yc.beta3,
               'Lambda': current_yc.ldb,
               'RSquared': r_squared
        }

        params_df = params_df.append(row, ignore_index=True)

    return params_df
