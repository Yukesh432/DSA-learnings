import os
import shutil
# .............................................................................................................

'''
On windows paths backshash(\) is used for path, and for linux forwardshash(/) as a separator
'''
## print out the current working directory
print(os.getcwd())

## change the current working directory
# os.chdir('/home/')
# .............................................................................................................

'''
The os.path.join is useful if we want to create strings of filenames or filepath
the below code will provide following output:
>>> /home/windows/fib.py
>>> /home/windows/LCS.py
>>> /home/windows/two.py

'''
print(os.path.join('usr', 'bin', 'spam'))

testfiles= ['fib.py', 'LCS.py', 'two.py']

for files in testfiles:
    print(os.path.join('/home/windows', files))

# .............................................................................................................

'''
Absolute path and relative path
a. os.path.abspath(path) will return string of the absolute path of the argument
b. os.path.isabs(path) will return bolean True or False acc to the given argument
c. os.path.relpath(path,start) will retrn a string of a relative path from the start path to path.

'''

print(os.path.isabs('.'))

print(os.path.abspath('.'))

print(os.path.relpath('/windows/projects', '/'))

# .............................................................................................................

'''
shutil(shell Utilities) module will allows to use shell command using python code.
'''