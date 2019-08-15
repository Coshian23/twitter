#!/usr/bin/env python
# coding: utf-8
  
from twitter import Twitter, OAuth

access_token = "1057214897946165248-xqkpkQIQQTi7AQRHjeOXrne4P9QPGk"
access_token_secret = "4VqE1WQxWpr7ysfiFgCxEplV6Ky5hMJpdVLTjs47oST0u"
api_key = "xTjNpPAMLpjNQgHUaIJcuLVQJ"
api_secret = "o8Dziw80QpOck4ThmOaO7kQbYJQgYLKb7JeGxsKpWC0q6nksKD"

t = Twitter(auth = OAuth(access_token, access_token_secret, api_key, api_secret))

searchTweets = t.search.tweets(q = "Qiita")

print(searchTweets)