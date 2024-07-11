import tweepy
import tweepy.client

# Replace these values with your own credentials
API_KEY = 'xxxxxxxxxxxxxxxxxxx'
API_KEY_SECRET = 'xxxxxxxxxxxxxxxxxxxxxx'
BREARER_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxx'

client = tweepy.Client(BREARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Upload image to Twitter. Replace 'filename' your image filename.
media_id = api.media_upload(filename="example.jpg").media_id_string
print(media_id)

# Text to be Tweeted
text = "Example Text"

# Send Tweet with Text and media ID
client.create_tweet(text=text, media_ids=[media_id])
print("Tweeted!")

