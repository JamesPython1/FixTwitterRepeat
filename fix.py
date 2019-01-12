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
fg = str(random.randint(50,5000000))
message = str(fg + " [PUT YOUR TEXT HERE]")
twitter.update_status(status=message)
