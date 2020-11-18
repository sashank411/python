import os
import zipfile

logzip = zipfile.ZipFile('C:\\Stories\\Fantasy\\archive.zip', 'w')

for folder, subfolders, files in os.walk('C:\\Stories\\Fantasy'):

    for file in files:
        if file.endswith('.pdf'):
            logzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)

logzip.close()
