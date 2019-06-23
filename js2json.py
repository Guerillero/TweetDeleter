import os

PATH_IN = r"A:\tweets" # Your tweets from your archive download
PATH_OUT = r"A:\TweetDeleter\data"
FILES_IN = os.listdir(PATH_IN)

for file in FILES_IN:
    fin = open(PATH_IN + "\\" + file, 'r')
    fout = open(PATH_OUT + "\\" + file + "on", 'w')
    for line in fin:
        li = line
        fout.write(li.replace("Grailbird.data.tweets_"+ file[:-3] + " = ", ""))
