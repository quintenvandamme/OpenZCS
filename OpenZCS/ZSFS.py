import os
import os.path

def AddFile(FileName,Directory):
    if os.path.isfile((Directory)+(FileName)):
        print("Errno: Folder already made")
    else: os.chdir(Directory)
    open(FileName, 'w')

def AddFolder(FolderDirectory):
    if os.path.exists(FolderDirectory):
       print("Errno: Folder already made")
    else: os.mkdir(FolderDirectory)

def File(FileName,Directory):
    if os.path.isfile((Directory)+(FileName)):
        file = open((Directory)+(FileName), 'r')
        print(file.read())
    else: print("Errno: No file called "+(FileName)+"")