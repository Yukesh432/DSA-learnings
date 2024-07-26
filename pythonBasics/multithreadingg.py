"""
If the task is I/O bound using multi-threading helps over mutiprocessing

Process: A process is an instance of a computer program that is in execution

Thread: A thread is an entity within a process that can be scheduled for execution

"""
import time
import threading

# start= time.perf_counter()

# def delay():
#     print("Making delay of 1 second")
#     time.sleep(1)
#     print("Delay finished.....")

# # delay()
# # delay()

# thread1= threading.Thread(target=delay)
# thread2= threading.Thread(target=delay)

# thread1.start()
# thread2.start()


# finish= time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds')

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


def takenap():
    time.sleep(5)
    print("Wake up!!!")


"""
Passing arguments to the Thread's target function

Eg: 

>>> import threading
>>> threadobj= threading.Thread(target= print, args=['Harry', 'Potter', 'Gilly'])
>>> threadobj.start()

Here target= function name
args= function argument

Without threading , we can simply run this line for printing::

>>> print('Harry', 'Potter', 'Gilly')

"""


"""
Multiple threads can cause the problem of concurrency issues.
This happens when threads read and write variables at the same time , causing threads to trip over each other.

"""

if __name__=='__main__':
    # main()
    threadobj1= threading.Thread(target= takenap)
    threadobj1.start()
    print("End of program............")