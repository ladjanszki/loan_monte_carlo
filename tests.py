import loanmc

# Testing YieldCurve class
yc = loanmc.YieldCurve(1, 2, 3, 0.1)
print(yc.calc(4))
print(yc.fit(4, 1, 2, 3, 0.1))
print(yc.fit(4, 2, 2, 2, 0.1))

exit(0)

# Testing the DataHandler class
dh = loanmc.DataHandler()
dh.import_xls('./historical_data/ZERO_2018.xlsx')
dh.import_xls('./historical_data/ZERO_2017.xlsx')
# dh.stats()
dh.to_csv('./historical_data/ZERO.csv')

# print(dh.df.head())
