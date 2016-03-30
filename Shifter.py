from Renamer import shiftName, cutSeconds, isValid
from os.path import isfile, join
import os

def shift(folder, seconds):
    if seconds==0:
        return
    files = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    files.sort(reverse=seconds > 0)
    for f in files:
        nameZones = os.path.splitext(f)
        name = nameZones[0]
        if isValid(name):
            ext = nameZones[1]
            newName = shiftName(name, seconds) + ext
            curFile = join(folder, f)
            newFile = join(folder, newName)
            os.rename(curFile, newFile)
            print(curFile, newFile)

def cut(folder):
    files = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    files.sort()
    for f in files:
        nameZones = os.path.splitext(f)
        name = nameZones[0]
        if isValid(name):
            ext = nameZones[1]
            newName = cutSeconds(name) + ext
            newFile = join(folder, newName)
            if isfile(newFile):
                os.remove(newFile)
            curFile = join(folder, f)
            os.rename(curFile, newFile)
            print(curFile, newFile)

folder = "d:\\photo\\picturesWork\\20151221"
#shift(folder, 60)
#cut(folder)

