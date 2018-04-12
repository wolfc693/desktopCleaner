''''##############################################
########### Create Directory Function ########
########### 2018 April #######################
########### Witten by: Scott Collins #########
########### Modified by: Cwwolf ##############
##############################################'''

import os


def makeDirectory(outFolder):
    if os.path.isdir(outFolder) == False:
        os.mkdir(outFolder)
    else:
        print("{} folder already exists...continuing".format(outFolder))
    return outFolder
