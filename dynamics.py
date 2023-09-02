"""File where the dynamics live."""
import numpy as np
import constants as c

# Function defining the system of first-order ODEs for 3D motion using r and v
def satellite_translational_eom(t,y):
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