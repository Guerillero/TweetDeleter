# TweetDeleter
I love [Semiphemeral](https://github.com/micahflee/semiphemeral) and I use it to
keep my recent tweets under control. However, it only has access to the last 3200
tweets accessible from the API. At my height, I had over 9000 tweets and I wanted
to do a Semiphemeral-like purge of all of my tweets from the last 6 years. All of
the tools that I found on the internet that worked off of the downloadable archive
were either paid, or deleted everything. So, I wrote these scripts.

To run these scrips you need Python 3 and tweepy installed on your computer.
(`pip install tweepy` should install the library) All other dependancies are '
either in this repo or in the standard library.

1. Download your [Twitter archive](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive)
2. Unzip the archive into a folder
3. Edit `settings.py` to add
  * the path to the folder with your tweets from the archive
  * the path to this folder
  * your twitter username
  * the minimum number of interactions to keep a tweet
4. Edit `secret.py` to add your Twitter API credentials
  * if you don't have a set of credentials, follow [this guide](https://python-twitter.readthedocs.io/en/latest/getting_started.html). You can use https://github.com/Guerillero/TweetDeleter as the website url of your app.
5. Run `js2json.py`
6. Run `delete.py`
