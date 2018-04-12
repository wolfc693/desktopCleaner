''''###########################################
########## Clean Images Function ##########
########## 2018 April #####################
########## Written by: cwwolf #############
###########################################'''

import os
import makeDirectory
import shutil

def cleanImages(inFolder, destination):
    fileList=os.listdir(inFolder)
    for entry in fileList:
        if entry[-4:]==".jpg":
            Jpeg=makeDirectory.makeDirectory(os.path.join(destination,entry[:-4]))
            shutil.move(os.path.join(inFolder,entry),Jpeg)
        elif entry[-4:]==".png":
            Png=makeDirectory.makeDirectory(os.path.join(destination,entry[:-4]))
            shutil.move(os.path.join(inFolder,entry),Png)
        else:
            nothingHappens=True