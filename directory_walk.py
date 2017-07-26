# Code snippet to walk through a directory and all subdirectories and place all the file names in a list
import os 

#The only thing that the user might specify is a filetype to limit on
myType = ".py"
myPath = "./"  # Current directory use a full path to search another tree
myFileList = []

for path, subdirs, files in os.walk(myPath):
        for name in files:
            if name.endswith(myType):
                f = os.path.join(path,name)
                myFileList.append(f)
                # Careful @ this point the path is specific to the directory which will change
                # depending on what system the data files are located.
                # 
                head,filedate = os.path.split(path)
                
print " The entire list ",myFileList
print " The list has ",len(myFileList), " entries"
