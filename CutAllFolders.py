from Renamer import cut
from os.path import isdir
import datetime

date = datetime.datetime(2016, 01, 01)
dateLimit = datetime.datetime(2016, 05, 01)
while True:
    folderName = datetime.datetime.strftime(date, '%Y%m%d')
    folder = "d:\\photo\\picturesHome\\" + folderName
    if isdir(folder):
        #print(date, folderName, 'yes')
        cut(folder)

    date = date + datetime.timedelta(days=1)
    if date > dateLimit:
        break
