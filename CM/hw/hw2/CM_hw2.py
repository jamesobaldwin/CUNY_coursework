import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt

mpl.style.use('mesa.mplstyle')

def E(t):
    return np.exp(-t**2)

# define E' for calculating Euler-Maclaurin error 
def Ep(t):
    return -2*t*np.exp(-t**2)

a = 0
b = 3

step = 0.1
# ensure range includes endpoint
x = np.arange(a, b+step, step) 

N = 10000
k = np.arange(1, N)
dx = (b - a) / N  # 3 / N
integral_vals = []

for i in x:
    # leading term (1/2)f(a) + (1/2)f(b)
    Eterm1 = (1/2)*E(a) + (1/2)*E(i)

    # integrate up to first x step
    mask_range = k*dx < i
    Eterm2 = np.sum(E(k[mask_range] * dx))

    # calculate integral result to this point
    Etot = dx * (Eterm1 + Eterm2)

    # store result
    integral_vals.append(Etot)

integral_vals = np.array(integral_vals)

# check valu against np.trapz
manual_trapz = integral_vals[-1]
print(manual_trapz)

trap = np.trapz(E(x), x, dx)
print(trap)

# error using manual 
print(f'Error from manual to np function: {np.abs(manual_trapz-trap):.4e}')

# error using Euler-Maclaurin
def euler_mac(f, a, b, h=0.1):
    return (1/12)*h**2*( f(a) - f(b) )

euler_mac_error = euler_mac(Ep, a, b, dx)
print('Euler-Maclaurin error: ', euler_mac_error)


#######################################################
# 0.8862073482539679
# 0.8862067342802126
# Error from manual (10000 steps) to np function: 6.1397e-07
# Calculated error using Euler-Maclaurin formula: 5.5534e-12
########################################################

#plot the trap method 
#plt.plot(x, integral_vals, label=r'$E(x)=%.4f"$'%manual_trapz)
#plt.title(r'Trapezoidal Method for $\int_0^x e^{-t^2} dt$')
#plt.xlabel('x (step size 0.1)')
#plt.grid(alpha=0.6)
#plt.ylabel('Integral Value')
#plt.show()
