import os

cwd=os.getcwd()                     #returns the current working directory as a string
# print(cwd)
for items in os.walk(cwd):     #returns generator object to walk through the current_working_dir, list_of_subfolders, list_of_files
    for f in items:
        print(f)
