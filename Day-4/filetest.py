import datetime
from package import File

f = File('.')

print(f.getMaxSizeFile(3)) 
# output : ['script.py', 'useME.py', 'dump.txt']

print(f.getLatestFiles(datetime.date(2025,4,7))) 
# output : ['dump.txt', 'useME.py']