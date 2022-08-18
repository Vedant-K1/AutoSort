#create a function to sort images and videos which are uploaded:
#TODO based on creation date
#TODO create a separate folder for each trip
#TODO One day, one subfolder in trip's folder
#TODO Default: Unsorted folder
#TODO Quick GUI for putting unsorted images into a folder/subfolder
#TODO Dockerize?
#TODO Combine with android app??
import glob
import os
from pathlib import Path


def sort_fldr_img(folder_name,trip):
    files = os.listdir(folder_name) #Getting the files
    print(files)
    print(len(files))

    for i in range(len(files)):
        files[i] = folder_name+files[i] #adding absolute path
        # print(i)
    # files.sort(key=lambda x: os.path.getmtime(x))
    paths = sorted(Path(folder_name).iterdir(), key=os.path.getctime) #sorting the files

    print(paths)



sort_fldr_img('C:\Vedant_\Projects\Sorting_System\Images','Test',)