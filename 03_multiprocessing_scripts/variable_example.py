import multiprocessing

def change_values(data, process_number):
    data.Value = process_number + 1



processes = []

data = multiprocessing.Value('i', 0)

for i in range(2):
    p = multiprocessing.Process(target=change_values, args=(data, i))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

    print(f'Main process is done {data.value}')