import tweepy

# boardgamenumber twitter account
CONSUMER_KEY = "arLDadWJYgNEWKC2fSbOZkN0m"
CONSUMER_SECRET = "tR4X1sVfh1FEcka1AC2KNi1zc1OVX5IWVhpOkuG4VuzWlEGsg2"
ACCESS_TOKEN = "890841149719552000-Qu94hUrO2vHVKEKV4ZnmT0K2NTIkw33"
ACCESS_SECRET = "BzNrsmMLCXLmZ9JPDee6P4oGCHYhVgTzdznPKIxWBc9cK"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

search_results = api.search(q="ボドゲ OR ボードゲーム", count=20)

for result in search_results:
    tweet_id = result.id
    user_id = result.user._json['id']
    try:
        #api.create_favorite(tweet_id)
        #api.retweet(tweet_id)
        api.create_friendship(user_id)
        print(user_id)
    except Exception as e:
        print(e)