import os
import settings

PATH_OUT = settings.root + "\\data"
FILES_IN = os.listdir(settings.twitterArchiveData)

if not os.path.exists(PATH_OUT):
    os.mkdir(PATH_OUT)

for file in FILES_IN:
    fin = open(settings.twitterArchiveData + "\\" + file, 'r')
    fout = open(PATH_OUT + "\\" + file + "on", 'w')
    for line in fin:
        li = line
        fout.write(li.replace("Grailbird.data.tweets_"+ file[:-3] + " = ", ""))
