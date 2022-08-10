import tweepy

#Authentication
auth = tweepy.0authHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create api object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")