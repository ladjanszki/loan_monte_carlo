import pandas as pd

import loanmc

import numpy as np

# Putting all excel data into a csv
# dh = loanmc.DataHandler()
# dh.import_xls('./historical_data/ZERO_2018.xlsx')
# dh.import_xls('./historical_data/ZERO_2017.xlsx')
# dh.to_csv('./historical_data/ZERO.csv')

# Loading data into DataHandler
dh = loanmc.DataHandler()
dh.read_csv('./historical_data/ZERO.csv')

# Fitting the model for all row
params_df = loanmc.fit_yield_curves(dh.df)

# # Original data in an animation
# loanmc.plot_yield_curves(dh.df, params_df)

# Testing the payment object
#yc = loanmc.YieldCurve(1, 2, 3, 0.1)

for rows in params_df.iterriws():

    yc = loanmc.YieldCurve(1, 2, 3, 0.1)

    pay = loanmc.Payment(1000000, 120, yc) 
    print(pay.calc_payment())





