import os.path
import glob

extensionList = {'.mkv','.avi'}
filmsPath = input('Please enter the path to the directory you want to order you movies in : ')
isDir = os.path.exists(filmsPath)
fileRegex = '[*]'
filesList = []

# Open folder
if isDir :
    for extention in extensionList :
        filesList+=(glob.glob(r'{0}\\[[]*.*[]]*{2}'.format(filmsPath, fileRegex, extention)))

#correct files' titles
[print(f) for f in filesList]