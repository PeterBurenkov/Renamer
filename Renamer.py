from os.path import isfile, join
import os
import datetime

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

def shiftName(name, seconds):
    zones = name.split('_')
    curDate = datetime.datetime.strptime(zones[1] + zones[2], '%Y%m%d%H%M%S')
    newDate = curDate + datetime.timedelta(seconds=seconds)
    newName = zones[0] + '_' + datetime.datetime.strftime(newDate, '%Y%m%d_%H%M%S')
    return newName

def cutSeconds(name):
    zones = name.split('_')
    curDate = datetime.datetime.strptime(zones[1] + zones[2], '%Y%m%d%H%M%S')
    newName = zones[0] + '_' + datetime.datetime.strftime(curDate, '%Y%m%d_%H%M')
    return newName

def isValid(name):
    zones = name.split('_')
    return zones[1].__len__() == 8 and zones[2].__len__() == 6
