import os
import makeDirectory
import shutil

def cleanEmails(inFolder, destination):
    fileList=os.listdir(inFolder)
    for entry in fileList:
        if entry[-4:]==".eml":
            files=makeDirectory.makeDirectory(os.path.join(destination,entry[:7]))
            shutil.move(os.path.join(inFolder,entry),files)
        else:
            nothingHappens=True