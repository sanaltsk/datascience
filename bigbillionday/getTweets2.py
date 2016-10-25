from twython import *
import unirest

#supply the appropriate value
TWITTER_APP_KEY = '*****' 
TWITTER_APP_KEY_SECRET = '*****' 
TWITTER_ACCESS_TOKEN = '******'
TWITTER_ACCESS_TOKEN_SECRET = '******'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

s = set()
keywords = ["#Flipkart","#BigBillionDay","#Flopkart","flipkart","#NoSale","#FlipkartSale","#bigbillionsale","#flopsale","#FekuFlops"]

for keyword in keywords:
    results = t.search(q=keyword,count=10000)
    if results.get('statuses'):
        for result in results['statuses']:
            s.add(result['text'])
        

print len(s)

file = open("tweets.csv","w")
pos = 0
neg = 0
neutral = 0
for i in s:
	response = unirest.post("https://text-sentiment.p.mashape.com/analyze",
  headers={"X-Mashape-Key": "IDBYuES9yHmshVmPgOXbDox5KBYfp1jowxdjsnFTEPS7hf6VTL"},
  params={"text": i})
  	try:
		positive = int(float(response.body['pos_percent'][:-1]))
		negative = int(float(response.body['neg_percent'][:-1]))
	except:
		print response.body
		continue
	details=str(positive)+","+str(negative)+","+i+'\n'
	file.write(details.encode('ascii', 'ignore'))
	if positive > negative:
		pos = pos+1
	elif positive < negative :
		neg = neg+1
	else:
		neutral = neutral + 1

string = "Positive : "+ str(pos) + "\nNegative :" + str(neg) + "\nNeutral :"+str(neutral)
file.write(string)
file.close()
