# import tweepy module to access twitter api 
import tweepy
# import json module for live streaming of tweets
import json

########## AUTHENTICATION TEST
#
# authenticate to twitter
#auth = tweepy.OAuthHandler("JLKFgAoS1zwP0OfQWWlgHxxWm", "PUs78WIfZvt1c8p3s2RuoAw2amBu1K6nIugy9WFI5xHEDVBKfM")
#auth.set_access_token("1261346688884563968-ATINPV1TxLWeOQwoAuf71vj4kdYpjP", "ZG42UePub8BygieMyOco7AtzmGRRfFqqXWwmS6ITqjjVy")

# create api object
#api = tweepy.API(auth)

#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during authentication")
#
##########  AUTHENTICATION TEST END 

########## MAIN TWITTER BOT 
# *** if using please comment out which api calls you do not require ***
#
#
# authenticate to twitter 
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")

# create api object and allow wait on rate limit so api notifies when we have exceeded the rate limit
api = tweepy.API(auth)

##### api call to be able to view 20 tweets from home timeline
#
#timeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{tweet.user.name} said {tweet.text}")
#####


##### creating a tweet for profile
#
#api.update_status("** Test tweet from Tweepy Python **")
#####


##### getting a users details 
#
# user = api.get_user("SanvittiSinha")
#
#print("User Details:")
#print(user.name)
#print(user.description)
#print(user.location)
#####


##### printing following last 20
#
#user = api.get_user("SanvittiSinha")
#
#print("Last 20 Followers:")
#for follower in user.followers():
#    print(follower.name)
#####


##### following users 
#
#api.create_friendship("sgxingh")
#####


##### update profile description
#
#api.update_profile(description="This account is made for Python Tweepy Testing ONLY")
#####


##### liking the most recent tweet in your timeline
#
#tweets = api.home_timeline(count=1)
#tweet = tweets[0]
#print(f"Liking tweet {tweet.id} of {tweet.author.name}")
#api.create_favorite(tweet.id)
#####


##### method for viewing blocked users
#  
#for block in api.blocks():
#    print(block.name)
#####


##### method for searching twitter for specific items based on text, language and many other filters *CHECK API DOCS FOR FURTHER INFO*
##### the below example searches twitter for public tweets in english and contain the word corona - the output will contain 10 results of latest tweets
#
#or tweet in api.search(q="Corona", lang="en", rpp=10):
#    print(f"{tweet.user.name}:{tweet.text}")
#####


##### how to view trending topics on twitter according to geographical location
##### in the below example we have used geographical location 1 which is worldwide please use api.trends_available() for location IDs
#
#trends_result = api.trends_place(1)
#for trend in trends_result[0]["trends"]:
#    print(trend["name"])
#####


##### streaming twitter to get realtime tweets
##### this service will constantely monitor twitter for new tweets and will instantly post them to you
##### please be aware to not exceed rate limit with this
#
#class MyStreamListener(tweepy.StreamListener):
#    def __init__(self, api):
#        self.api = api
#        self.me = api.me()
#
#    def on_status(self, tweet):
#        print(f"{tweet.user.name}:{tweet.text}")
#
#    def on_error(self, status):
#        print("Error detected")
#
# authenticate to twitter 
#auth = tweepy.OAuthHandler("JLKFgAoS1zwP0OfQWWlgHxxWm", "PUs78WIfZvt1c8p3s2RuoAw2amBu1K6nIugy9WFI5xHEDVBKfM")
#auth.set_access_token("1261346688884563968-ATINPV1TxLWeOQwoAuf71vj4kdYpjP", "ZG42UePub8BygieMyOco7AtzmGRRfFqqXWwmS6ITqjjVy")
#
# create api object for streaming
#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#
# create tweets listener
#tweets_listener = MyStreamListener(api)
#stream = tweepy.Stream(api.auth, tweets_listener)
#stream.filter(track=["Corona", "Health", "Deaths"], languages=["en"])
#####


##### tweepy models - use thse to carry out multiple API operation
##### tweepy can encapsulate the responses from various twitter api methods. This gives you a way to use the results
##### in the below example we fetch every tweet in which we are mentioned then like each one and follow the author
#
#tweets = api.mentions_timeline()
#for tweet in tweets:
#    tweet.favorite()
#    tweet.user.follow()
#####


##### cursors in tweepy - view multiple paginated data items
##### cursors in tweepy allow you to view a larger set of data if it is paginated 
##### in the below example rather than displaying 20 latest tweets we can view 100 tweets using the cursor method 
#
#for tweet in tweepy.Cursor(api.home_timeline).items(100):
#    print(f"{tweet.user.name} said: {tweet.text}")
#####