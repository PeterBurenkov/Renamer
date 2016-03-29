import datetime
def shiftName(name, seconds):
    zones = name.split('_')
    _checkLength(zones[1], zones[2])
    curDate = datetime.datetime.strptime(zones[1] + zones[2], '%Y%m%d%H%M%S')
    newDate = curDate + datetime.timedelta(seconds=seconds)
    newName = zones[0] + '_' + datetime.datetime.strftime(newDate, '%Y%m%d_%H%M%S')
    return newName

def cutSeconds(name):
    zones = name.split('_')
    _checkLength(zones[1], zones[2])
    curDate = datetime.datetime.strptime(zones[1] + zones[2], '%Y%m%d%H%M%S')
    newName = zones[0] + '_' + datetime.datetime.strftime(curDate, '%Y%m%d_%H%M')
    return newName

def _checkLength(zone1, zone2):
    if zone1.__len__() < 8 or zone2.__len__() < 6:
        raise ValueError()
