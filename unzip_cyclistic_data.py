import py7zr
import os


zips = os.listdir('Data')
for zipName in zips:
    with open(os.path.join('Data', 'cyclisticData.7z'), 'ab') as f:
        with open(os.path.join('Data', zipName), 'rb') as z:
                  f.write(z.read())
                  
with py7zr.SevenZipFile(os.path.join('Data', 'cyclisticData.7z'), "r") as archive:
    archive.extractall(path = 'Data')
    
