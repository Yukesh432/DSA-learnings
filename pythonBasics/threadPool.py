"""
- The asynchronous execution can be done with the help of ThreadPoolExecutor.
python concurrent.futures have the class named : ThreadPoolExecutor and ProcessPoolExecutor

ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously

"""
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time

def testFunc(numlist: np.array):
    print(numlist)
    return sum(numlist)


"""
Deadlock:: It can occur when the callable assocaited with a Future waits on the result if another Future

"""

def wait_b():
    time.sleep(5)
    print(b.result())
    return 5

def wait_a():
    time.sleep(5)
    print(a.result())
    return 6



if __name__=='__main__':
    import os
    print("Testing 123....")
    with ThreadPoolExecutor(max_workers=1) as executor:
        future= executor.submit(testFunc, np.ones(5))
        print(future.result())


        with ThreadPoolExecutor(60) as exe:
          
            print(exe._max_workers)

    print(".............")
    executor_ii= ThreadPoolExecutor(max_workers=os.cpu_count())
    a= executor_ii.submit(wait_b)
    b= executor_ii.submit(wait_a)
