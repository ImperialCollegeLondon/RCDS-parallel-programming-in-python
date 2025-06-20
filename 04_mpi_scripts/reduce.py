# Run this script with the terminal command `mpiexec -n 4 python reduce.py`

import mpi4py.MPI as MPI
import numpy as np

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_rank = comm.Get_size()

# We're going to generate 10 random numbers between 0 and 1 and count how many are less than 0.5
n = 10

# Calculate how many numbers each rank will generate
n_local = int(n / n_rank)
if rank < n % n_rank:
    # If the rank is less than the remainder, it will generate one more number
    # This is to ensure that the right number of numbers are generated
    n_local += 1

# Generate the random numbers and check how many are less than 0.5
numbers_local = np.random.rand(n_local)
count_local = np.sum(numbers_local < 0.5)

# Print the local data on each rank
print(f'Rank {rank} has generated {n_local} numbers, and {count_local} are less than 0.5')

# Reduce the count of numbers less than 0.5 from all ranks to rank 0
count = comm.reduce(count_local, op=MPI.SUM, root=0)

# Rank 0 now has the total count
if rank == 0:
    print(f'Rank {rank} has the overall result of {count} numbers less than 0.5')
else:
    # Reduce returns None on all ranks other than the root
    print(f'On rank {rank}, the value of count is {count}')

# If we want all ranks to have the total count, we can use allreduce
# This does not require a root rank
count_all = comm.allreduce(count_local, op=MPI.MIN)

print(f'On rank {rank}, the value of count_all is {count_all}')
