import random
import time
import multiprocessing

# Define the function to be called by each process
def count_points_inside_circle(n_points, queue):
    # Calculate the number of points inside the circle and adds it to the queue

    # Initiate the variable to store the number of points inside the circle
    n_inside_local = 0
    for i in range(n_points):
        # Generate a random point
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1:
            # If the point is inside the circle, increment the counter
            n_inside_local += 1

    # Add the number of points inside the circle to the queue
    queue.put(n_inside_local)

if __name__ == '__main__':
    # Note the starting time
    start_time = time.time()

    # Number of points to generate
    n_points = int(1e7)

    # Number of processes to use
    n_processes = 4

    # Create the queue
    queue = multiprocessing.Queue()

    for i in range(n_processes):
        # Start the processes
        p = multiprocessing.Process(target=count_points_inside_circle, args=(n_points // n_processes, queue))
        p.start()

    # Initiate the variable to store the total number of points inside the circle
    n_points_inside_circle = 0

    for i in range(n_processes):
        # Add the number of points inside the circle
        # There is no need to wait for the processes to finish as get blocks until the result is available
        n_points_inside_circle += queue.get()

    # Calculate the value of pi
    pi_approximation = 4 * n_points_inside_circle / n_points

    print(f'The value of pi is approximately {pi_approximation}')

    print(f'Time taken: {time.time() - start_time}')