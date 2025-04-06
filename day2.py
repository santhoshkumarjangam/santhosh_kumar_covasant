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

'''
output :
file with the max size is: 3.txt
size is:170 bites
'''
