import os
import zipfile
from datetime import date,datetime

class LogArchival:

    def __init__(self):
        self.time=datetime.now()
        self.year=self.time.strftime("%Y")
        self.month=self.time.strftime("%m")
        self.day=self.time.strftime("%d")

obj=LogArchival()
time=obj.time
folder_name="ReachClient_"+str(obj.year)+str(obj.month)+str(obj.day)
print(time)
print(folder_name)
