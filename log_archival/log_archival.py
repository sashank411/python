import os,time,zipfile
from datetime import date,datetime

# DEFINING 'ZIP' CLASS
class Zip:
    def __init__(self, source, destination, header):
        if not os.path.isdir(destination):
            print("The destination_path:\t'%s'\tdoes not exist....\nCreating the said destination directory:"%destination)
            os.mkdir(destination)
            print("Destination directory created.")
        self.src=source
        self.dst=destination
        self.hdr=header
        # if __name__ = "__main__": self.zip(self.src,self.dst,self.hdr)

    def zip(self,source=self.src,destination=self.dst,header=self.hdr):
        logzip = zipfile.ZipFile('C:\\Stories\\Fantasy\\archive.zip', 'w')
        for folder, subfolders, files in os.walk('C:\\Stories\\Fantasy'):
            for file in files:
                if file.endswith('.pdf'):
                    logzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)
        logzip.close()

# CONFIGURATION SETTINGS
source_path="D:\simulation\MconnectPlus\ReachAdmin"#include a '\' at the end
target_path="D:\simulation\MconnectPlus\Archives_India\ReachAdmin" #include a '\' at the end
log_header="ReachAdmin_"
# span="01:59:59"

# SET DESTINATION PATH
time=datetime.now()
directory_name=log_header+time.strftime("%Y""%m""%d")
destination_path=os.path.join(target_path,directory_name)

# FUNTION CALL
zipper=Zip(source_path,destination_path,log_header)
