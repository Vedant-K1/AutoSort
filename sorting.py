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


def sort_fldr_img(folder_name,trip,default='Unsorted'):
    files = list(filter(os.path.isfile, glob.glob(folder_name + "*")))
    files.sort(key=lambda x: os.path.getmtime(x))
    print(files)
    type(files)


def