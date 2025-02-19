# Run this code with the following command: mpiexec -n 4 python share_price.py

import mpi4py.MPI as MPI
import numpy as np
from scipy.stats import norm

def simulate_share_price(initial_price, daily_change_mean, daily_change_std, n_days):
    """
    Simulates the price of a share over a number of days.

    Parameters:
    initial_price (float): The initial price of the share.
    daily_change_mean (float): The average daily fractional change in the share price.
    daily_change_std (float): The standard deviation of the daily fractional change in the share price.
    n_days (int): The number of days to simulate.

    Returns:
    float: The simulated share price after n_days.
    """

    return initial_price * norm.rvs(loc=1 + daily_change_mean, scale=daily_change_std, size=n_days).prod()

# Input parameters
initial_price = 100
daily_change_mean = 0.001
daily_change_std = 0.02
n_days = 100
n_simulations = 1000

# Get the rank and size of the MPI communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Calculate the number of simulations each rank will perform
n_simulations_per_rank = n_simulations // size
if rank < n_simulations % size:
    n_simulations_per_rank += 1

# Perform the simulations
local_results = np.asarray([simulate_share_price(initial_price, daily_change_mean, daily_change_std, n_days) for _ in range(n_simulations_per_rank)])

square_local_results = local_results ** 2

# Sum and summarise local values
total_local_results = local_results.sum()
total_local_square_results = square_local_results.sum()
local_min = np.min(local_results)
local_max = np.max(local_results)

# Gather the results from all ranks
total_results = comm.reduce(total_local_results, op=MPI.SUM, root=0)
total_square_results = comm.reduce(total_local_square_results, op=MPI.SUM, root=0)
minimum = comm.reduce(local_min, op=MPI.MIN, root=0)
maximum = comm.reduce(local_max, op=MPI.MAX, root=0)

if rank == 0:
    mean = total_results / n_simulations
    std = np.sqrt(total_square_results / n_simulations - mean ** 2)
    print(f"Mean: {mean}")
    print(f"Standard deviation: {std}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

