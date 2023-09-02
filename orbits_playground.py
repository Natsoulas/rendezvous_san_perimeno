"""File where the simulation playground lives."""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import constants as c 
from tools import kepler2rv
from dynamics import satellite_translational_eom


# Lets get an initial plot of the two orbits

# Starting with initial orbital elements, I convert them to an initial position and time.

r_helper_initial, v_helper_initial = kepler2rv(c.a*1000,c.e, np.deg2rad(c.raan), np.deg2rad(c.i),0,0,c.mu_earth)
r_target_initial, v_target_initial = kepler2rv(c.a_t*1000,c.e_t, np.deg2rad(c.raan_t), np.deg2rad(c.i_t),0,0,c.mu_earth)
# Propagate the two orbits in order to get a plot.
# P^2 = a^3
period_helper = np.sqrt(c.a**3)
period_target = np.sqrt(c.a**3)

end_time = 60000

# Time points for integration
t = np.linspace(0, end_time, 10000)
t_target = np.linspace(0, end_time, 10000)

# Numerical integration using odeint:
# Helper Initial Orbit:
r_v_helper_initial = np.concatenate((r_helper_initial,v_helper_initial))

# Target Initial Orbit:
r_v_target_initial = np.concatenate((r_target_initial, v_target_initial))

result_helper = sp.integrate.solve_ivp(satellite_translational_eom, [0,end_time], r_v_helper_initial,t_eval=t, method='RK45', rtol=1e-12, atol=1e-12)
result_target = sp.integrate.solve_ivp(satellite_translational_eom, [0,end_time], r_v_target_initial,t_eval=t_target, method='RK45', rtol=1e-12, atol=1e-12)


# Extracting position components
x_positions = result_helper.y[0, :]
y_positions = result_helper.y[1, :]
z_positions = result_helper.y[2, :]

x_pos_target = result_target.y[0,:]
y_pos_target = result_target.y[1,:]
z_pos_target = result_target.y[2,:]

plot1 = plt.figure(1)
plt.plot(t,x_positions)
plt.title("Helper Satellite x-position")
plt.ylabel("x positiion (meters)")
plt.xlabel("time (seconds)")

plot2 = plt.figure(2)
plt.plot(x_positions,y_positions)
plt.title("Helper Satellite Orbit")
plt.xlabel("x-position (m)")
plt.ylabel("y-position (m)")


plot3 = plt.figure(3)
ax = plt.axes(projection='3d')
# Data for a three-dimensional plot
ax.scatter3D(x_positions,y_positions,z_positions, 'red')
ax.scatter3D(x_pos_target,y_pos_target,z_pos_target,'gray')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

plot4 = plt.figure(4)
relative_positions = result_helper.y[:3,:] - result_target.y[:3,:]
relative_distances = np.apply_along_axis(np.linalg.norm, 0, relative_positions)
plt.plot(t, relative_distances)
plt.title("Relative distance between orbits vs. time")
plt.ylabel("time (s)")
plt.ylabel("Magnitude of relative distance")

