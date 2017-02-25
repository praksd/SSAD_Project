from twython import     Twython


class twitterfeeds(object):
    title = ""



def scrape(query):
	twitter =       Twython('f3eoMS4R7zRtR0IFcK8LXcIei',    'kJAAjsu3rrn5Qf4MXXpXDnpLvKzTcoaMhQZVokEnEvluVJvbRq')
        my_twitterfeeds = []
	for     status in twitter.search(q= query)["statuses"]:
        	user= status["user"]["screen_name"].encode('utf-8')
        	if user != 'iiit_hyderabad':
                        twfeeder = twitterfeeds()
                	user = status["user"]["screen_name"].encode('utf-8')
                	text = status["text"].encode('utf-8')
                        twfeeder.title = user +  ":" + text
                        my_twitterfeeds.append(twfeeder)
                	print user,     ":", text
                	print
        return my_twitterfeeds  

        
