import math
import numpy as np
import multiprocessing
import time

def get_permutation(lst, n):
    '''
    Gets the nth permutation of a list

    Parameters: 
    lst (list): A list
    n (int): The index of the permutation

    Returns:
    list: The nth permutation of the list
    '''

    # Create a local copy of the list
    lst = lst.copy()

    # Create a list of factorials
    factorials = [math.factorial(i) for i in range(0, len(lst))]
    factorials.reverse()

    # Create a list to store the permutation
    permutation = []

    # Loop through the factorials
    for i in factorials:
        # Get the index of the number to add
        index = n // i

        # Add the number to the permutation
        permutation.append(lst[index])

        # Remove the number from the list
        lst.pop(index)

        # Update n
        n = n % i

    return permutation

def get_city_distances(filepath='data/city_distances.csv'):
    '''
    Returns a list of distances between cities from a csv file

    Parameters:
    filepath (str): The path to the csv file

    Returns:
    list: The names of cities
    numpy.ndarray: The distances between cities
    '''

    # Read the csv file
    full_data = np.genfromtxt(filepath, delimiter=',', dtype='str')

    # Get the city names
    city_names = full_data[0, 1:]

    # Get the distances between cities
    distances = full_data[1:, 1:].astype(float)

    return city_names, distances


def get_total_route_length(route, distances):
    '''
    Returns the total length of a route

    Parameters:
    route (list): A list of city indices
    distances (numpy.ndarray): A 2D array of distances between cities

    Returns:
    float: The total length of the route
    '''

    # Create a variable to store the total length
    total_length = 0

    # Loop through the route
    for i in range(len(route) - 1):
        # Get the distance between the cities
        total_length += distances[route[i], route[i + 1]]

    # Add the distance from the last city to the first city
    total_length += distances[route[-1], route[0]]

    return total_length

def find_shortest_route_permutation(distances, i_first, i_last, queue):
    '''
    Finds the shortest loop around all cities in a certain range of permutations
    
    Parameters:
    distances (numpy.ndarray): A 2D array of distances between cities
    i_first (int): The first index of the permutation range
    i_last (int): The last index of the permutation range
    queue (multiprocessing.Queue): A queue to store the results
    
    Returns:
    None
    '''

    # Create variables to store the shortest distance and route
    shortest_distance = None
    shortest_route = None

    # Create a list of indexes
    # We will use permutations of this list to generate routes to consider
    indexes_list = list(range(distances.shape[0]))

    # Loop through the indexes of the permutations
    for i in range(i_first, i_last + 1):
        # Get the permutation of the current index
        route = get_permutation(indexes_list, i)

        # Get the total length of the route of this permutation
        total_length = get_total_route_length(route, distances)

        if shortest_distance is None or total_length < shortest_distance:
            # If this is the shortest route so far, update the shortest distance and route
            shortest_distance = total_length
            shortest_route = route
            # Add the first city to the end of the route to make it a loop
            shortest_route.append(route[0])

    # Put the shortest distance and route in the queue
    queue.put((shortest_distance, shortest_route))

# Using the multiprocessing module means we only need to run this script from the main process
start_time = time.time()

# Get the city names and distances
city_names, distances = get_city_distances()

# Set up the number of processes and permutations
n_processes = 4
n_permutations = math.factorial(distances.shape[0])
n_permutations_per_process = n_permutations // n_processes
queue = multiprocessing.Queue()

for i in range(n_processes):
    # Find the range of permutations for this process
    i_first = int(i * n_permutations_per_process)
    if i == n_processes - 1:
        # If this is the last process, the last index is the last permutation
        i_last = n_permutations - 1
    else:
        i_last = int((i + 1) * n_permutations_per_process - 1)
    # Spawn and start the processes
    # The results will be stored in the Queue
    p = multiprocessing.Process(target=find_shortest_route_permutation, args=(distances, i_first, i_last, queue))
    p.start()

# Create variables to store the shortest distance and route from all processes
shortest_distance = None
shortest_route = None

for i in range(n_processes):
    # Get the shortest distance and route from the queue
    shortest_distance_from_process, shortest_route_from_process = queue.get()
    if shortest_distance is None or shortest_distance_from_process < shortest_distance:
        # If this is the shortest route so far, update the shortest distance and route
        shortest_distance = shortest_distance_from_process
        shortest_route = shortest_route_from_process

# Create a string of city names for the shortest route
shortest_route_city_names = ", ".join([city_names[i] for i in shortest_route])

# Print the results
print(f'The shortest route is {shortest_route_city_names} with a total length of {shortest_distance}km')

# Print the time taken
print(f'Time taken: {time.time() - start_time}s')









