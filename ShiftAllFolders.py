from Renamer import shift
from os.path import isfile, join, isdir
import datetime

date = datetime.datetime(2016, 3, 25)
dateLimit = datetime.datetime(2016, 3, 30)
while True:
    folderName = datetime.datetime.strftime(date, '%Y%m%d')
    folder = "d:\\photo\\picturesHome\\" + folderName
    if isdir(folder):
        #print(folder, folderName, 'yes')
        shift(folder, -60)

    date = date + datetime.timedelta(days=1)
    if date > dateLimit:
        break

