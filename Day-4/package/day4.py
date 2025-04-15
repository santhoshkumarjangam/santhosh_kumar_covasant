#Q5
class Poly:
    
    def __init__(self,*args):
        self.lst = list(args)
        
    def __str__(self):
        return f"Poly({self.lst})"
        
    def __add__(self,other):
        if len(self.lst)<=len(other.lst):
            result = other.lst.copy()
            for i in range(-1,(len(self.lst)+1)*(-1),-1):
                result[i] += self.lst[i]
            return Poly(*result)
        else:
            result = self.lst.copy()
            for i in range(-1,(len(other.lst)+1)*(-1),-1):
                result[i] += other.lst[i]
            return Poly(*result)
            
#Q6
class File:
    
    def __init__(self,path):
        self.path = path
        
    def getMaxSizeFile(self,limit=1):
        import os
        files_with_sizes = {}
        
        for dir_path, dir_name, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(dir_path, file)
        
                file_size = os.path.getsize(file_path)

                files_with_sizes[file] = file_size
                
        sorted_files = list(dict(sorted(files_with_sizes.items(), key=lambda item: item[1],reverse=True)).keys())
        
        return sorted_files[:limit]
        
        
    def getLatestFiles(self,date):
        import os
        from datetime import datetime
        
        files_with_dates = {}
        
        for dir_path, dir_name, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(dir_path, file)
        
                creation_time = os.path.getctime(file_path)
                
                creation_date = datetime.fromtimestamp(creation_time)

                creation_date_readable = creation_date.strftime("%Y-%m-%d")
                
                files_with_dates[file] = creation_date_readable
                
                
        result = []
        for file, c_date in files_with_dates.items():
            if c_date >= str(date):
                result.append(file)
                
        return result