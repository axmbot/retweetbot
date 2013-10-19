# -*- coding: utf-8 -*-

import twitter
import urllib2, urllib, json, simplejson

#brings in API key
from tweetkey import api


"""
Welcome to the Group Retweet Bot.

These are the variables for this bot. You'll need to customize your users (i.e., the folks you want to retweet);
the checkvariable, which is the hashtag you're checking for; and the bot's user handle.  Everything else should run smoothly
from there.

The example is below is implemented for @88_bartenders, a group account for 88 Bar's bloggers. 88 Bar is a popular
blog about Chinese tech and design. Check us out at http://www.88-bar.com!
"""

#Set your user acronym and handles here. Acronyms should be the key. Handle should be the value.
grouphandles = {'AXM':'anxiaostudio',
              'JL':'jasonli',
              'TW':'triciawang',
              'LJ':'lynj',
              'JG':'jingejinge',
              'GW':'gwbstr',}

#This is the hashtag you want to check for retweeting
checkvariable = '#88'

#This is the bot's user handle
bothandle = '88_bartenders'



"""
This is the actual bot application.

If everything's good above, this should run smoothly. Nothing below needs to be customized per se.
"""

#function to acquire the json for a web page at x. Useful for searching Twitter.
def jsonjson(x):
     req = urllib2.Request(x)
     opener = urllib2.build_opener()
     instance = opener.open(req)
     return simplejson.load(instance)
     
#This removes the checkvariable from a tweet. Used for posting the tweet.
def remcheckvariable(string):
    newstring = []
    for word in string.split():
        if not word == checkvariable:
            newstring.append(word)
    return ' '.join(newstring)

#Removes acronyms from tweets. Used for testing against already tweeted tweets.
def remacronym(acronym, string):
    newstring = []
    for word in string.split():
        if not word == acronym:
            newstring.append(word)
    return ' '.join(newstring)


#Pulls tweets the bot has already tweeted. This avoids having to set up a databae, simply checks against what's out there.
alreadytweeted = []
bababa = jsonjson('https://api.twitter.com/1/statuses/user_timeline.json?count=200&screen_name=%s&include_rts=1&include_entities=true' % bothandle)
for tweet in bababa:
    for key in grouphandles.keys():
        newtweet = remacronym(str("^" + key), tweet['text'])
        alreadytweeted.append(newtweet)

#Pulls the group's tweets, places in a dict called grouptweets
grouptweets = {}
for user in grouphandles.items():
    acronym = user[0]
    handle = str(user[1])
    acronym = api.GetUserTimeline(handle)
    grouptweets[str(user[0])] = []
    for x in acronym:
        grouptweets[str(user[0])].append(x.text)
    
#Checks for the checkvariable and retweets it with the user's acronym appended. Flags if the retweet is longer than 140.
for user in grouptweets:
    for tweet in grouptweets[user]:
        if remcheckvariable(tweet) in alreadytweeted:
            pass
        elif checkvariable in tweet:
            retweet = remcheckvariable(tweet) + " ^" + str(user)
            if len(retweet) <= 140:
                try:
                    api.PostUpdate(retweet)
                    confirmmessage = "Helper bot says: I've posted your tweet, saying '" + retweet[0:30] + "...'"
                    api.PostDirectMessage(str(grouphandles[user]), confirmmessage)
                except:
                    pass
            else:
                #This sends a direct message to the user if their original tweet is a little too long to retweet.
                retweeterror = "Helper bot says: You need to shorten your post by " + str(abs(140 - len(retweet))) + " characters before I can retweet."
                api.PostDirectMessage(str(grouphandles[user]), retweeterror)
        else:
            pass