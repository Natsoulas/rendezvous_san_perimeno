"""The file where the visualizations live."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read history df from csv.
history_df = pd.read_csv('first_trial.csv')
# Grab postion vectors from both the helper and target.
z_helper_history = history_df["Helper State History"].values
# Make a relative distance (magnitude) vs time plot.

# Make a 3d plot of both satellites' trajectories over the course of the whole simulation.