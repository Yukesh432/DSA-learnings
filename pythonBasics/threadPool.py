"""
- The asynchronous execution can be done with the help of ThreadPoolExecutor.
python concurrent.futures have the class named : ThreadPoolExecutor and ProcessPoolExecutor

ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously

"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import numpy as np


def testFunc(numlist: np.array):
    print(numlist)
    return sum(numlist)

if __name__=='__main__':
    print("Testing 123....")
    with ThreadPoolExecutor(max_workers=1) as executor:
        future= executor.submit(testFunc, np.ones(5))
        print(future.result())


        with ThreadPoolExecutor(60) as exe:
            # report the number of workers in the pool
            print(exe._max_workers)