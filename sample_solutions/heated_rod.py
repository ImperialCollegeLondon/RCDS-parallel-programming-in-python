import numpy as np
import multiprocessing
import random
import matplotlib.pyplot as plt

def find_peak_temeprature(boundary_temeprature, heating_rate, rod_length, diffusion_coefficient, n_points):
    '''
    Find the peak staedy state temperature in a rod heated at a constant rate.
    
    Parameters

    boundary_temperature (float): The temperature of the rod at the left and right boundaries.
    heating_rate (float): The rate at which the rod is heated.
    rod_length (float): The length of the rod.
    diffusion_coefficient (float): The diffusion coefficient of the rod.
    n_points (int): The number of points to use in the numerical solution.
    '''

    dx = rod_length / (n_points - 1)

    # Create the heat diffusion matrix
    diffusion_matrix = np.zeros((n_points, n_points))
    np.fill_diagonal(diffusion_matrix, -2 * diffusion_coefficient / dx ** 2)
    np.fill_diagonal(diffusion_matrix[1:], diffusion_coefficient / dx ** 2)
    np.fill_diagonal(diffusion_matrix[:, 1:], diffusion_coefficient / dx ** 2)

    # Set the boundary conditions
    diffusion_matrix[0, 0] = 1
    diffusion_matrix[0, 1] = 0
    diffusion_matrix[-1, -1] = 1
    diffusion_matrix[-1, -2] = 0

    rhs = np.full(n_points, -heating_rate)
    rhs[0] = boundary_temeprature
    rhs[-1] = boundary_temeprature

    # Solve the system of equations
    temperature = np.linalg.solve(diffusion_matrix, rhs)

    # Find and return the peak temperature
    peak_temperature = np.max(temperature)

    return peak_temperature

def make_histogram(data):
    '''
    Make a histogram of the data and save it to a file.
    
    Parameters
    
    data (array_like): A list of data to plot. Could be a list, Numpy array, etc
    
    Returns
    
    None
    '''
    plt.hist(data, bins=20, density = True)
    plt.xlabel('Peak Temperature')
    plt.ylabel('Probability Density')
    plt.title('Histogram of Peak Temperature')
    plt.savefig('outputs/peak_temperature_histogram.png')

if __name__ == '__main__':
    # Define the number of samples to generate and number of processes to use
    n_samples = int(1e5)
    n_processes = 4
    
    # Create a list of arguments for the function
    arguments = [(300, 10, 10, 0.9 + 0.2 * random.random(), 100) for _ in range(n_samples)]
    # Create a pool of processes
    with multiprocessing.Pool(n_processes) as pool:
        # Use the pool to calculate the results
        # Use starmap to pass the arguments to the function
        # The results will be returned in a list
        results = pool.starmap(find_peak_temeprature, arguments)
    # We can pass the results straight to the plotting function
    make_histogram(results)