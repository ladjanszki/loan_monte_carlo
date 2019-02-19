import loanmc

import unittest

dh = loanmc.DataHandler()
dh.import_xls('./historical_data/ZERO_2018.xlsx')
dh.import_xls('./historical_data/ZERO_2017.xlsx')
# dh.stats()
dh.to_csv('./historical_data/ZERO.csv')

# print(dh.df.head())
