'''
Based on code from here https://realpython.com/python-matplotlib-guide/
'''

import matplotlib.pyplot as plt
import numpy as np

# Creating a single figure with a single axes object in it
# plt.subplots can be called as plt.subplots(nrows=1, ncols=1) to get more than one axes
# fig, ax = plt.subplots()


rng = np.arange(50)
#print(rng)
rnd = np.random.randint(0, 10, size=(3, rng.size))
print(rnd)
print(type(rnd))

yrs = 1950 + rng
print(yrs)


# This creates one axes and sets the figsize
fig, ax = plt.subplots(figsize=(5,3))
ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'oceania'])

ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()
print(type(fig))
print(type(ax))

plt.show()
