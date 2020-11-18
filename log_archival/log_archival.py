import os,time,zipfile
from datetime import date,datetime

# DEFINING 'ZIP' CLASS
class Zip:
    def __init__(self, source, destination):
        if not os.path.isdir(destination):
            print("The destination directory does not exist....\nCreating the said destination directory:")
            os.mkdir(destination)
            print("Destination directory created.")
        self.src=source
        self.dst=destination

# CONFIGURATION SETTINGS
source_path=""#include a '\' at the end
target_path=""#include a '\' at the end

# SET DESTINATION PATH
time=datetime.now()
directory_name=time.strftime("%Y""%m""%d")
destination_path=target_path+directory_name

# FUNTION CALL
zipper=Zip(source_path,destination_path)
