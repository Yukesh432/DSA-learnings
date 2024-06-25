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

eg. shutil.copy(source, destination) will copy the file . Both source and destination are string. 
If destination is a filename, it will be used as the new name of the copied file

shutil.copy() returns the string of the copied path file.

'''

newdir_name= 'pythonBasics'
full_path= os.path.join(os.path.abspath('.'), newdir_name)
# print(full_path)

newdir= os.makedirs(full_path, exist_ok= True)
print(newdir)
shutil.copy('sortbylen.py', full_path)
print('COPIED SUCCESSFUL......')

# # Moving files using shutil
# filename= 'iterator.py'
# destination_path= os.path.join(os.path.abspath('.'), newdir_name)
# source_path= os.path.join(os.path.abspath('.'), filename)
# shutil.move(source_path,destination_path)
# print("FILE MOVED SUCESSFULLY!!!")

# .............................................................................................................

'''
shutil.copy() will copy the single file whereas shutil.copytree() will copy an entire
folder and every folder and files contained within it.
The function will return the path of the copied folder as string

shutil.copytree(source, destination)

'''
def copytreefunc(*args):
    # dirname= 'DataStruct'

    for idx, item in enumerate(args):
        source_path= os.path.join(os.path.abspath('.'), item)
        print(source_path)
        # destination_path= os.path.join(os.path.abspath('.'), )


copytreefunc(['test.py', 'sortbylen.py'])