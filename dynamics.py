"""File where the dynamics live."""
import numpy as np
import constants as c
import scipy as sp

# Functions defining the systems of first-order ODEs for 3D motion using r and v.
def target_satellite_eom(t,y):
    """
    r[0]: x position
    r[1]: y position
    r[2]: z position
    v[0]: x velocity
    v[1]: y velocity
    v[2]: z velocity
    """
    r = y[:3]
    v = y[3:6]
    norm_r = np.linalg.norm(r)  # Norm of the position vector
    
    # Equations of motion
    drdt = v
    dvdt = -c.mu_earth * r / (norm_r**3)
    return np.array([drdt[0],drdt[1],drdt[2],dvdt[0],dvdt[1],dvdt[2]])

def helper_satellite_eom(t,y,ux,uy,uz):
    """
    r[0]: x position
    r[1]: y position
    r[2]: z position
    v[0]: x velocity
    v[1]: y velocity
    v[2]: z velocity
    u: Force from thruster performing translational control
    """
    r = y[:3]
    v = y[3:6]
    u = np.array([ux,uy,uz])
    norm_r = np.linalg.norm(r)  # Norm of the position vector
    
    # Equations of motion
    drdt = v
    dvdt = (-c.mu_earth * r / (norm_r**3)) + u/c.m
    return np.array([drdt[0],drdt[1],drdt[2],dvdt[0],dvdt[1],dvdt[2]])

def integrate_states_forward(z_helper,z_target,F_control, seconds_forward):
    """Numerically integrate dynamics for the rendezvous simulation loop. Step forward by input quantity of seconds."""
    z_helper_plus_x_seconds = sp.integrate.solve_ivp(helper_satellite_eom, [0,seconds_forward], z_helper, method='RK45', rtol=1e-12, atol=1e-12, t_eval=[seconds_forward],args=F_control)
    z_target_plus_x_seconds = sp.integrate.solve_ivp(target_satellite_eom, [0,seconds_forward], z_target, method='RK45', rtol=1e-12, atol=1e-12, t_eval=[seconds_forward])
    return z_helper_plus_x_seconds, z_target_plus_x_seconds