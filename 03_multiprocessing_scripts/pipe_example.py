import multiprocessing
import numpy

def calculate_sum(conn):
    # Wait to receive an array from the parent process
    array = conn.recv()
    # Calculate the sum of the array
    result = numpy.sum(array)
    # Send the result back to the parent process
    conn.send(result)

# Create a Pipe() object
# This function returns a pair of connection objects connected by a pipe
parent_conn, child_conn = multiprocessing.Pipe()
# Create a process and pass the child connection object to it
# The process will implement the calculate_sum function
p = multiprocessing.Process(target=calculate_sum, args=(child_conn,))
# Start the process
p.start()
# Send an array to the child process
parent_conn.send(numpy.arange(1, 6))
# Receive the result from the child process
print(parent_conn.recv())
# Wait until the process is finished
p.join()
print('Main process is done')