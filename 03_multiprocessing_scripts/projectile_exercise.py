import math
import random
import time

def calculate_range(angle, velocity):
    '''Calculate the range of a projectile given an angle and velocity
    Assumes no air resistance and a flat surface
    Inputs:
    angle: float, angle in degrees
    velocity: float, velocity in m/s
    Outputs:
    range_projectile: float, range of the projectile in metres
    '''

    # Calculate the time of flight
    time_of_flight = 2 * velocity * math.sin(math.radians(angle)) / 9.81

    # Calculate the range
    range_projectile = velocity * math.cos(math.radians(angle)) * time_of_flight

    return range_projectile

def calculate_range_distribution(n_samples, n_bins, min_angle, max_angle, min_velocity, max_velocity):
    '''Calculate the range of a projectile given a range of angles and velocities
    Assumes no air resistance and a flat surface
    Inputs:
    n_samples: int, number of samples to generate
    n_bins: int, number of bins to divide the range into
    min_angle: float, minimum angle in degrees
    max_angle: float, maximum angle in degrees
    min_velocity: float, minimum velocity in m/s
    max_velocity: float, maximum velocity in m/s
    Outputs:
    bin_boundaries: list, boundaries of the bins in metres
    bin_counts: list, number of samples in each bin
    '''

    # Find the angle that gives the maximum range
    if min_angle < 45 and max_angle > 45:
        max_range_angle = 45
    elif min_angle < 45:
        max_range_angle = max_angle
    else:
        max_range_angle = min_angle

    # Find the maximum and minimum ranges
    max_range = calculate_range(max_range_angle, max_velocity)
    min_range = min(calculate_range(min_angle, min_velocity), calculate_range(max_angle, min_velocity))

    # Create the bins
    bin_boundaries = [min_range + i * (max_range - min_range) / n_bins for i in range(n_bins + 1)]
    bin_counts = [0] * n_bins

    for i in range(n_samples):
        # For each sample, generate a random angle and velocity
        angle_current = random.uniform(min_angle, max_angle)
        velocity_current = random.uniform(min_velocity, max_velocity)

        # Find the range of the projectile
        range_current = calculate_range(angle_current, velocity_current)

        # Find the bin that the range falls into and increment the counter for that bin
        i_bin = int((range_current - min_range) / (max_range - min_range) * n_bins)
        bin_counts[i_bin] += 1

    return bin_boundaries, bin_counts

start_time = time.time()

# Define the parameters
n_samples = int(1e7)
n_bins = 20
min_angle = 30
max_angle = 31
min_velocity = 99
max_velocity = 100


# Calculate the bin boundaries and counts
bin_boundaries, bin_counts = calculate_range_distribution(n_samples, n_bins, min_angle, max_angle, min_velocity, max_velocity)
end_time = time.time()

# Print the outputs
for i in range(len(bin_boundaries) - 1):
    print(f'Range: {bin_boundaries[i]:,.2f}m-{bin_boundaries[i + 1]:,.2f}m: {bin_counts[i]:,}')

# Print the running time
print(f'Time taken: {end_time - start_time}s')