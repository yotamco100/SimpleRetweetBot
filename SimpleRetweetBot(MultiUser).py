import twitter #import Twitter API

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''
twitter = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
#authenticate with Twitter Apps (temp. private acc.)

handle = []
lastTweetId = []
#arrays of handles and status IDs
#add a new 0 on the lastTweetId array for every handle, or else it crashes (can someone fix?)

for x in range(len(handle)):
    lastTweetId[x] = twitter.GetUserTimeline(screen_name=handle[x], include_rts=False, count=1)[0].id
#fills in initial Status IDs

while(True): 
    for x in range(len(handle)):
        newTweet = twitter.GetUserTimeline(screen_name=handle[x], include_rts=False, count=1)[0].id
        if (newTweet > lastTweetId[x]):
            print("New tweet from {} with ID {}. Retweeting...".format(handle[x], newTweet))
            twitter.PostRetweet(newTweet)
            print("Retweet successful. Waiting...")
            lastTweetId[x] = newTweet

#infinite loop for continous running of the shell. checks for a new tweet ID and if that ID is newer, it retweets it,
#then changes lastTweetId to that newest tweet ID

