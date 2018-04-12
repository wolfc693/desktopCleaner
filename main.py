''''##############################################
######### GUI version of Desktop Cleaner #########
######### 2018 April #############################
######### Written by: wolfc693 ###################
######### Version 1.1.0 ##########################
##################################################
############# ChangeLog ##########################
# New version incorporates cleaning function #####
# for emails related to UMUC work ################
##################################################'''

from Tkinter import *
import random
import cleanImages
import cleanWordDocs
import cleanEmails
import cleaning
import sys

# FUNCTIONS
def stopProgram():
    root.destroy()


# Building Environment
root = Tk()
root.configure(bg='red')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Path to the Desktop; Enter the path between the sets of double quotes
inFolder = r""
destination = r""

# Create Header Label Greeting
headerLabel = Label(topFrame,
                    text="Desktop Cleaner GUI \n\nSelect file types you want moved\n into folders on the Desktop.").grid(
    row=0)

# Creating Checkboxes
var1 = IntVar()
Checkbutton(topFrame, text="Word Documents", variable=var1).grid(row=1, column=0, sticky=W)
var2 = IntVar()
Checkbutton(topFrame, text="Images", variable=var2).grid(row=2, column=0, sticky=W)
var3 = IntVar()
Checkbutton(topFrame, text="Emails", variable=var3).grid(row=1, column=1, sticky=W)

# Creating Buttons
button1 = Button(bottomFrame, text="Clean!",
                 command=lambda: cleaning.cleaning(var1, var2, var3, inFolder, destination)).grid(row=3, column=1,
                                                                                                  sticky=W)
button2 = Button(bottomFrame, text="Exit", command=lambda: stopProgram()).grid(row=3, column=2)

# Maintains Environment
root.mainloop()
