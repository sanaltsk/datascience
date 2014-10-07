from twython import *
import unirest

#supply the appropriate value
TWITTER_APP_KEY = 'TqDEKbl5kdZ4yhtD6AdaX98kW' 
TWITTER_APP_KEY_SECRET = 'oXTBQqP2I8SZcUBl0hDtLCij64kkJPx6SJIjd4Fp0Vt0A5rFdP' 
TWITTER_ACCESS_TOKEN = '13758412-n33Qh3nL2GPkpdFDxg906hyeqv9cfIJ4BS6VdxNsg'
TWITTER_ACCESS_TOKEN_SECRET = 'BbnInN2lsO3zRcTAZZDcDnrzxBSxcSwliqH2WQRjBBoPO'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#Flipkart', count=4000)

s = set()
tweets = search['statuses']
i = 0
for tweet in tweets:
  i=i+1  
  #print i,tweet['text'],'\n'
  s.add(tweet['text'])
  
search2 = t.search(q='#BigBillionDay', count=4000)

tweets2 = search2['statuses']
i = 0
for tweet in tweets2:
  i=i+1  
  #print i,tweet['text'],'\n'
  s.add(tweet['text'])

search3 = t.search(q='#Flopkart', count=4000)

tweets3 = search3['statuses']
i = 0
for tweet in tweets3:
  i=i+1  
  #print i,tweet['text'],'\n'
  s.add(tweet['text'])

search4 = t.search(q='flipkart', count=4000)

tweets4 = search4['statuses']
i = 0
for tweet in tweets4:
  i=i+1  
  #print i,tweet['text'],'\n'
  s.add(tweet['text']) 
 
file = open("tweets.csv","w")
pos = 0
neg = 0
neutral = 0
for i in s:
	response = unirest.post("https://text-sentiment.p.mashape.com/analyze",
  headers={"X-Mashape-Key": "IDBYuES9yHmshVmPgOXbDox5KBYfp1jowxdjsnFTEPS7hf6VTL"},
  params={"text": i}
)
	positive = response.body['pos_percent'][:-1]
	negative = response.body['neg_percent'][:-1]
		
	details=positive+","+negative+","+i+'\n'
	file.write(details.encode('ascii', 'ignore'))
	if int(float(positive))>int(float(negative)):
		pos = pos+1
	elif int(float(positive))<int(float(negative)) :
		neg = neg+1
	else:
		neutral = neutral + 1

string = "Positive : "+ str(pos) + "\n Negative :" + str(neg) + "\n Neutral :"+str(neutral)
file.write(string)
file.close()
  