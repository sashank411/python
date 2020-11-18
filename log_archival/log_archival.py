import os
import zipfile
from datetime import date,datetime

class LogArchival:

    def __init__(self):
        self.time=datetime.now()
        self.folder_name=self.time.strftime("%Y""%m""%d")

obj=LogArchival()
name=obj.folder_name
folder_name="ReachClient_"+str(name)
print(folder_name)
