''''####################################
########## Clean Word Documents ####
########## 2018 April ##############
########## Written by: cwwolf ######
####################################'''

import os
import makeDirectory
import shutil

def cleanWordDocs(inFolder, destination):
    fileList=os.listdir(inFolder)
    for entry in fileList:
        if entry[-4:]==".doc" or entry[-5:]==".docx":
            if entry[:4].isalpha()==True and entry[4:7].isdigit()==True:
                files=makeDirectory.makeDirectory(os.path.join(destination,entry[:7]))
                shutil.move(os.path.join(inFolder,entry),files)
            else:
                NothingHappens=True
        else:
            nothingHappens=True