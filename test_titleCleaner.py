import os
import glob
import re

extensionList = {'.mkv','.avi'}
filmsPath = input('Please enter the path to the directory you want to order you movies in : ')
isDir = os.path.exists(filmsPath)
filesList = []

# Open folder
if isDir :
    for extention in extensionList :
        filesList+=(glob.glob(r'{0}\\[[]*.*[]]*{1}'.format(filmsPath, extention)))

#correct files' titles
titleStart = r'\[.*[.].*\] '
#[print(re.sub(titleStart,'',f)) for f in filesList]
[os.rename(f, re.sub(titleStart,'',f)) for f in filesList]