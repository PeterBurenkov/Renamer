from Renamer import cut
from os.path import isdir
import datetime

date = datetime.datetime(2016, 1, 3)
dateLimit = datetime.datetime(2016, 3, 29)
while True:
    folderName = datetime.datetime.strftime(date, '%Y%m%d')
    folder = "d:\\photo\\picturesWork\\" + folderName
    if isdir(folder):
        #print(date, folderName, 'yes')
        cut(folder)

    date = date + datetime.timedelta(days=1)
    if date > dateLimit:
        break
