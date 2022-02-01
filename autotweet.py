#build Twitter Which Auto Tweet's Qoutes every 5 mintues   Date: 1/02/2022


import tweepy
import pandas as pd
import time

import pandas as pd
df = pd.read_csv(r'C:\\twitter\\Autoquotestwitterbot\\GreatQuotes.csv', on_bad_lines='skip', sep=';') #Here on '' Upload your Quotes.csv File Location
df.shape 


latest_tweet_number = 0


print(latest_tweet_number)


def tweet_now(msg):
    msg = msg[0:270]
    try:
      auth = tweepy.OAuthHandler("",  "")  #Enter Api and Secret key's here
      auth.set_access_token("","")  #Enter Access and  Secret Token's here
      api = tweepy.API(auth)
      try:
            api.verify_credentials()
            print("Authentication OK")
      except:
            print("Error during authentication")
      api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True)
      api.update_status(msg)
      print(msg)

      print("Tweeted")
    
    except Exception as e:
      print(e)

def tweet():
  for idx, rows in df.iterrows():
    if idx <= latest_tweet_number:
      continue
        
    hashtags = '#Quotes #QuotestoLiveby #QuotesOfTheDay '
    tweet_now(rows['QUOTE']  + '\n\n\n' + '\n\n\n' + hashtags)
    print("done")
    time.sleep(300)
    print('ok')


tweet()


















