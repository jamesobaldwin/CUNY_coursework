import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt

mpl.style.use('mesa.mplstyle')

def deltoid(theta):
    x = 2 * np.cos(theta) + np.cos(2*theta)
    y = 2 * np.sin(theta) - np.sin(2*theta)
    return x,y

def polar_plot(theta_fn, theta_range):
    theta = np.linspace(*theta_range)
    r = theta_fn(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x,y

# define the Galilean spiral function
def galilean_spiral(theta):
    return theta**2

# define Fey's function
def fey_fn(theta):
    return np.exp(np.cos(theta)) - 2 * np.cos(4*theta) + np.sin(theta/12)**5

# define param space to be between 0 and 2pi for a deltoid curve
theta_vals_deltoid = np.linspace(0, 2*np.pi, 10000)

# define param space for Galilean spiral and Fey's
gal_spiral_range = (0, 10*np.pi, 10000)
fey_range = (0, 24*np.pi, 10000) 

# store the x, y values for the deltoid curve
x_vals_deltoid, y_vals_deltoid = deltoid(theta_vals_deltoid)
# store the x, y values for the Galilean spiral
x_vals_gal, y_vals_gal = polar_plot(galilean_spiral, gal_spiral_range)
# store vals for Fey's function 
x_vals_fey, y_vals_fey = polar_plot(fey_fn, fey_range)

# create a row of subplots, 3 cols wide
plt.close('all')
fig, axs = plt.subplots(1,3, figsize=(25,10))

# plot the deltoid curve
axs[0].plot(x_vals_deltoid, y_vals_deltoid)
axs[0].set_xlabel("x")
axs[0].set_ylabel('y')
axs[0].set_title(r"Deltoid Curve $0<\theta<2\pi$")

# plot the Galilean spiral
axs[1].plot(x_vals_gal, y_vals_gal)
axs[1].set_xlabel(r"$x=r\cos(\theta)$")
axs[1].set_ylabel(r'$y=r\sin(\theta)$')
axs[1].set_title(r"Galilean Spiral $0<\theta<10\pi$")

# plot Fey's function 
axs[2].plot(x_vals_fey, y_vals_fey)
axs[2].set_xlabel(r"$x=r\cos(\theta)$")
axs[2].set_ylabel(r'$y=r\sin(\theta)$')
axs[2].set_title(r"Fey's Function $0<\theta<24\pi$")

#plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=1, hspace=0.4)

fig.tight_layout()
plt.savefig('hw1_plots.png')
plt.show()

# plot the Galilean spiral and Fey's in polar
# fig, axs_polar = plt.subplots(1,2)
# plt.suptitle("Polar Coordinates")
# 
# theta_gal = np.linspace(*gal_spiral_range)
# axs_polar[0].plot(galilean_spiral(theta_gal), theta_gal)
# axs_polar[0].set_title("Galilean Spiral")
# axs_polar[0].set_xlabel("r")
# axs_polar[0].set_ylabel("theta")
# 
# theta_fey = np.linspace(*fey_range)
# axs_polar[1].plot(fey_fn(theta_fey), theta_fey)
# axs_polar[1].set_xlabel("r")
# axs_polar[1].set_ylabel("theta")
# axs_polar[1].set_title("Fey's Function")

# plt.show()
