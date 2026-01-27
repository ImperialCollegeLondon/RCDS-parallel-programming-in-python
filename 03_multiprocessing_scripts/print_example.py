import multiprocessing

def greeting(processes_number):
    print(f'Hello from process number {processes_number}')

processes = []

print(__name__)

for i in range(2):
    p =multiprocessing.Process(target=greeting, args=(i,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print('Main process is done')