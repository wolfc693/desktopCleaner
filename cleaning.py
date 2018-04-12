import cleanWordDocs
import cleanEmails
import cleanImages


def cleaning(var1,var2,var3,inFolder,destination):
    if var1.get()==1 and var2.get()==1 and var3.get():
        cleanWordDocs.cleanWordDocs(inFolder, destination)
        cleanImages.cleanImages(inFolder, destination)
        cleanEmails.cleanEmails(inFolder, destination)
    elif var1.get()==1 and var2.get()==1 and var3.get()!=1:
        cleanWordDocs.cleanWordDocs(inFolder, destination)
        cleanImages.cleanImages(inFolder, destination)
    elif var1.get()==1 and var2.get()!=1 and var3.get()==1:
        cleanWordDocs.cleanWordDocs(inFolder, destination)
        cleanEmails.cleanEmails(inFolder, destination)
    elif var1.get()!=1 and var2.get()==1 and var3.get()==1:
        cleanImages.cleanImages(inFolder, destination)
        cleanEmails.cleanEmails(inFolder, destination)
    elif var1.get()==1:
        cleanWordDocs.cleanWordDocs(inFolder, destination)
    elif var2.get()==1:
        cleanImages.cleanImages(inFolder, destination)
    elif var3.get()==1:
        cleanImages.cleanImages(inFolder, destination)
    else:
        nothingHappens=True