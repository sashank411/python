import os.path, time
date_modified = time.ctime(os.path.getmtime("D:\SetUps\WinDev2010Eval.ova"))
print("Last modified: %s" %date_modified )
# print("Created: %s" % time.ctime(os.path.getctime("test.txt")))
