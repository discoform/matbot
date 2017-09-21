'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'ITRp8luPK4n3xDeEppikloipt'
MY_CONSUMER_SECRET = 'AzoasaJb5IuJGiAEywZEM9QPaaBhTWoU8bS8AalaGOqyRu1Ikd'
MY_ACCESS_TOKEN_KEY = '805893830755041281-fs8Z4BncftqOhaNppmvehVYNWytnA8f'
MY_ACCESS_TOKEN_SECRET = 'GNHDPPUeyDc6pgLg3uZt9Xp7T5XfF5hqkx0Moj9gTr63S'

SOURCE_ACCOUNTS = ["DesignerDepot"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 5 #How often do you want this to run? 1/8 times?
ORDER = 4 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "_matbot" #The name of the account you're tweeting to.
