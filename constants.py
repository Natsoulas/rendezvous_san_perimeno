"""File to store vehicle and physics constants."""
# Helper Satellite Starting Orbit Parameters:
a = 7155 # km
e = 0.0
i = 98 # degrees
# w is not assigned (have to determine?)
raan = 52 # degrees

# Target Orbit Parameters:
a_t = 7167 # km
e_t = 0.0
i_t = 99 # degrees
# w_t is not assigned (have to determine?)(set to zero until further notice)
raan_t = 42 # degrees

# Helper Satellite Properties:
m = 500 # kg
thrust =0.450 # Newtons
isp = 2200 # seconds
mu_earth = 3.986E14 # m^3/s^2
Cd = 2.2 # Drag Coefficient
Area = 1 # m^2
rho_atmosphere = 1e-6 #kg/m^3 (general estimate)

# Control Law constants (still need tuning):
# Best tuning so far K1 = 0.0000001, K2 = 0.0000001
K0 = 1
K1 = 1
K2 = 1000