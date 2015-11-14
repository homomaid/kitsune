from twython import Twython

APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

f = open('count.txt', 'r+')
count = f.readline()
twitter.update_status(status="きつねかわいい！！！(" + count + "回目)")
f.seek(0)
f.write(str(int(count) + 1))
f.close()
