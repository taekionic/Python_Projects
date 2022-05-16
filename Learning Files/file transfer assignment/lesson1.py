import shutil
import os

#set where the sourse of files are
source = 'C:\\Users\\Cagol\\OneDrive\\Documents\\GitHub\\Python_Projects\\Learning Files\\file transfer assignment\\folderA\\'

#set destination path

destination = 'C:\\Users\\Cagol\\OneDrive\\Documents\\GitHub\\Python_Projects\\Learning Files\\file transfer assignment\\folderB\\'
files = os.listdir(source)

for i in files: 
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
