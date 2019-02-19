import loanmc

# Testing YieldCurve class
yc = loanmc.YieldCurve(1, 2, 3, 0.1)
print(yc.calc(4))
print(yc.fit(4, 1, 2, 3, 0.1))
print(yc.fit(4, 2, 2, 2, 0.1))

