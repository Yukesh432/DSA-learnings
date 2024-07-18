"""
If the task is I/O bound using multi-threading helps over mutiprocessing
"""
import time
import threading

start= time.perf_counter()

def delay():
    print("Making delay of 1 second")
    time.sleep(1)
    print("Delay finished.....")

# delay()
# delay()

thread1= threading.Thread(target=delay)
thread2= threading.Thread(target=delay)

thread1.start()
thread2.start()


finish= time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

import itertools
import time
import sys

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'): 
        status = char + ' ' + msg 
        write(status) 
        flush() 
        write('\x08' * len(status)) 
        time.sleep(.1) 
        if not signal.go: 
            break 
    write(' ' * len(status) + '\x08' * len(status))

def slow_function(): 
    # pretend waiting a long time for I/O 
    time.sleep(3) 
    return 42

def supervisor(): 
    signal = Signal() 
    spinner = threading.Thread(target=spin, args=('thinking!', signal)) 
    print('spinner object:', spinner) 
    spinner.start() 
    result = slow_function() 
    signal.go = False 
    spinner.join() 
    return result 

def main(): 
    result = supervisor() 
    print('Answer:', result)


if __name__=='__main__':
    main()