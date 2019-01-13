from twython import Twython
import random

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)

listofnum = list(range(1,1000000))
numb = random.choice(listofnum)
print(numb)
fg = str(numb)
listofnum.remove(numb)

message = str(fg + " [PUT YOUR TEXT HERE]")
twitter.update_status(status=message)
