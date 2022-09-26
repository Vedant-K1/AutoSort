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
from PIL import Image


def image_path(folder_name,trip):
    files = os.listdir(folder_name) #Getting the files
    print(files)
    print(len(files))

    for i in range(len(files)):
        files[i] = folder_name+'\\\\'+files[i] #adding absolute path
        # print(i)
        # files.sort(key=lambda x: os.path.getmtime(x))
    paths = sorted(Path(folder_name).iterdir(), key=os.path.getmtime) #sorting the files
    files.sort(key=os.path.getmtime)
    print(paths)
    # return(paths)
    sort_img(files)
    make_dir(folder_name,paths,trip)


def sort_img(files):
    p=len(files)
    Mdate=[]
    cnt=0
    for i in files:
        print('i:',i,' ',cnt)
        try:
            Mdate.append(get_date_taken(i))
            print('Date created: ', Mdate[cnt], '\n')
        except:
            print('ERROR IN DATE TAKEN IN:',i,'\n')

        cnt+=1
    print(Mdate)


def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def make_dir(folder_name,paths,trip):
    target_dir='C:\Vedant_\Projects\Sorting_System\Target'
    direc=os.path.join(target_dir,trip)#Making the absolute path of the main directory of trip
    mode = 0o666
    try:
        os.mkdir(direc,mode)#Directory made
        print("Made directory:",direc)
    except:
        print("Error in making Directory:",direc)

    #MAKING SUB-DIRECTORIES
    days=5
    d={}
    day_path=os.path.join(direc)

#-----------------------MAIN--------------------------------

print('Starting Auto Sort')
sorted_path=image_path('C:\Vedant_\Projects\Sorting_System\Images','Test',)
#bruh


'''
Base Directory is 'C:\Vedant_\Projects\Sorting_System\Images' also known as the dump directory.
Pics - unsorted,random,etc

Test: Trip name
Target directory: C:\Vedant_\Projects\Sorting_System\Target

'''
