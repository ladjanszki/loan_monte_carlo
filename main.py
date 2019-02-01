from scipy.optimize import newton
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constructing a yield curve
def yield_curve(t, b1, b2, b3, ld_t):
    
    t1 = b1
    t2 = b2 *  ((1 - np.exp(-ld_t * t)) / (ld_t * t))
    t3 = b3 *  ((1 - np.exp(-ld_t * t)) / (ld_t * t) * np.exp(-ld_t * t))

    return (t1 + t2 + t3)


# A torlesztes utan visszamaradt osszeg
def remaining(c, H, T, r):
    '''
    c: A torlesztoreszlet
    H: Felvett hitelosszeg
    T: futamido
    '''

    rem = H
    for t in range(T):
        #r = 0.02  # Hozamgorbe (egyelore vizszintes)
        exc = 0.03  # Kockazati felar
        k = (r[t] / 100.00) + exc  # Kamat amit a bank ker

        rem = rem * (1 + k) - c
    return rem


# MAIN
H = 1224963
T = 15

t = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00, 15.00]
r = [1.00, 1.00, 2.00, 2.50, 3.00, 3.50, 3.00, 4.00, 5.00,  7.00,  6.00,  4.00,  4.00,  4.00,  4.00]

print(len(r))
print(len(t))

#for i in t:
#    r.append(yield_curve(i, 7, -1, -0.1, 0.3))

# A torleszto kiszamolasa solverrel
C_res = newton(remaining, 10000, args=(H, T, r))
print("havi torleszto: " + str(C_res / 12.0))


if not abs(remaining(C_res, H, T, r)) < 10e-8:
    print("nem konvergalt")

plt.plot(t, r)
plt.show()
 


    
     


        
    
