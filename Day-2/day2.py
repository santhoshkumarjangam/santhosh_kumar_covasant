
#Q3:

# IMPLEMENTATION 1
import os

base = "/Users/hp/oneDrive/Desktop/dir_demo"
max_size = -1
max_sized_file = ""

for dir_path, dir_name, files in os.walk(base):

    for file in files:
        file_path = os.path.join(dir_path, file)
        
        file_size = os.path.getsize(file_path)

        if file_size > max_size:
            max_sized_file = file
            max_size = file_size

print(f"file with the max size is: {max_sized_file}")
print(f"size is:{max_size} bites")

#---------------------------------------------------------------

#IMPLEMENTATION 2
import glob
import os

base = "/Users/hp/oneDrive/Desktop/dir_demo"
max_size = -1
max_sized_file = ""

iter = glob.iglob("**/*.txt", root_dir=base, recursive=True)

for file in iter:
    file_path = os.path.join(base, file)
    file_size = os.path.getsize(file_path)

    if file_size > max_size:
            max_sized_file = file
            max_size = file_size
            
print(f"file with the max size is: {max_sized_file}")
print(f"size is:{max_size} bites")

'''
OUTPUT :
file with the max size is: 3.txt
size is:170 bites
'''


#Q4:

import glob
import os

base = r"."

iter = glob.iglob("**/*", root_dir = base, recursive = True)

with open('dump.txt', 'w') as f:
    for file in iter:
        file_path = os.path.join(base, file)
        f.write(file_path + '\n')

with open("dump.txt", "r") as f:
    lines = f.readlines()
    print(lines)

#OUTPUT:
#['./dump.txt\n', '.\mex.py\n', '.\mex_test.py\n', '.\script.py\n', '.\useME.py\n']

#dump.txt:
'''
    ./dump.txt
    .\mex.py
    .\mex_test.py
    .\script.py
    .\useME.py
'''
