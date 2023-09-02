"""File where the controls live."""
import numpy as np
import constants as c

# Reference Tracking Control Law
def orbit_controller(z,m_sc,K1,K2):
    """Orbit Controller: Outputs desired Thrust to follow a reference orbit
    for translational motion in cartesian coordinates. Reference frame is earth
    inertial."""
	#z = [r_deputy, v_deputy, r_deputy_desired, v_deputy_desired]
    r_deputy = z[:3]
    v_deputy = z[3:6]
    r_deputy_desired = z[6:9]
    v_deputy_desired = z[9:12]
    # a_kep is an anonymous function 
    a_kep = lambda r,mu: -(mu/(np.linalg.norm(r)**3))*r
    Deltar = r_deputy - r_deputy_desired
    Deltar_d = v_deputy - v_deputy_desired
    A = a_kep(r_deputy, c.mu_earth)
    B = a_kep(r_deputy_desired, c.mu_earth)
    F_com = -(A-B) - c.K1*Deltar - c.K2*Deltar_d
    F_command = F_com*m_sc
    
    # Actuator saturation occurs if commanded thrust is more than thruster can produce.
    # Therefore, it is capped at the thruster's maximum (c.thrust).
    if np.linalg.norm(F_command) > c.thrust:
        multiplier = np.linalg.norm(F_command)/c.thrust
        F_command = F_command/multiplier
    return F_command, Deltar, Deltar_d, A, B