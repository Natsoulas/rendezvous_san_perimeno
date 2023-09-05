"""The file where the main utility of this repository is executed."""

import numpy as np
import pandas as pd
from simulate_rendezvous import run_rendezvous_sim
from tools import kepler2rv
import constants as c


# Set up initial conditions (state).
r_helper_initial, v_helper_initial = kepler2rv(c.a*1000,c.e, np.deg2rad(c.raan), np.deg2rad(c.i),0,0,c.mu_earth)
r_target_initial, v_target_initial = kepler2rv(c.a_t*1000,c.e_t, np.deg2rad(c.raan_t), np.deg2rad(c.i_t),0,0,c.mu_earth)
z_helper_initial = np.concatenate((r_helper_initial,v_helper_initial))
z_target_initial = np.concatenate((r_target_initial, v_target_initial))
# Set up convergence criteria for the simulation. (May need tuning)
r_conv_criteria = 1000 # Relative distance must be less than 10 meters.
v_conv_criteria = 10000 # Difference in velocities should be less than 0.1 m/s in magnitude.
conv_criteria = [r_conv_criteria, v_conv_criteria]

# Run rendezvous simulation.
t_history, z_helper_history, z_target_history, F_control_history, rel_distance_history, rel_speed_diff_history = run_rendezvous_sim(z_helper_initial, z_target_initial, conv_criteria)

# Save off history arrays into a pandas df.
history_df = pd.DataFrame(data = {'Time History':t_history, 'x_helper_history':z_helper_history[:,0], 'y_helper_history':z_helper_history[:,1], 'z_helper_history':z_helper_history[:,2],
                                  'x_target_history':z_target_history[:,0], 'y_target_history':z_target_history[:,1], 'z_target_history':z_target_history[:,2],
                                  'Ux History':F_control_history[:,0], 'Uy History':F_control_history[:,1], 'Uz History':F_control_history[:,2],
                                  'dist_x_history':rel_distance_history[:,0], 'dist_y_history':rel_distance_history[:,1], 'dist_z_history':rel_distance_history[:,2]})
# Save df as a csv in subdirectory for generating visuals.

history_df.to_json('sim_trial.json')