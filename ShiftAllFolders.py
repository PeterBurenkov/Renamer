from Renamer import shift
from os.path import isfile, join, isdir
import datetime

date = datetime.datetime(2016, 2, 2)
dateLimit = datetime.datetime(2016, 3, 29)
while True:
    folderName = datetime.datetime.strftime(date, '%Y%m%d')
    folder = "d:\\photo\\picturesWork\\" + folderName
    if isdir(folder):
        #print(date, folderName, 'yes')
        shift(folder, 25)

    date = date + datetime.timedelta(days=1)
    if date > dateLimit:
        break

