from Renamer import shiftName, cutSeconds
from os.path import isfile, join
import os

def shift(seconds):
    folder = 'SomeFiles'
    files = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    for f in files:
        nameZones = os.path.splitext(f)
        name = nameZones[0]
        ext = nameZones[1]
        newName = shiftName(name, seconds) + ext
        curFile = join(folder, f)
        newFile = join(folder, newName)
        print(curFile, newFile)
        os.rename(curFile, newFile)

def cut():
    folder = 'SomeFiles'
    files = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    for f in files:
        nameZones = os.path.splitext(f)
        name = nameZones[0]
        ext = nameZones[1]
        newName = cutSeconds(name) + ext
        curFile = join(folder, f)
        newFile = join(folder, newName)
        print(curFile, newFile)
        os.rename(curFile, newFile)

#shift(10)
cut()