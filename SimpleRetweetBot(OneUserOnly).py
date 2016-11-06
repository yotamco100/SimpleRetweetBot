import twitter #import Twitter API

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''
twitter = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
#authenticate with Twitter Apps (add your own twitter keys)

handle = ""
lastTweetId = twitter.GetUserTimeline(screen_name=handle, include_rts=False, count=1)[0].id

while(True):
    newTweet = twitter.GetUserTimeline(screen_name=handle, include_rts=False, count=1)[0].id
    if (newTweet > lastTweetId):
        print("New tweet from {} with ID {}.".format(handle, newTweet))
        twitter.PostRetweet(newTweet)
        print("Retweet successful. Waiting...")
        lastTweetId = newTweet
