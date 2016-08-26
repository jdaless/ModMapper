import praw
import urllib.request as url
from html.parser import HTMLParser
import time
import warnings
warnings.filterwarnings("ignore")

class ModListScraper(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self, convert_charrefs = True)
		self.moderatorOf = []
		self.parserInSubs = False

	def handle_starttag(self, tag, attrs):
		if(tag == 'ul' and len(attrs) > 0 and attrs[0] == ('id', 'side-mod-list')):
			self.parserInSubs = True

	def handle_endtag(self, tag):
		if(tag == 'ul' and self.parserInSubs):
			self.parserInSubs = False

	def handle_data(self, data):
		if(self.parserInSubs):
			if("/r/" in data):
				self.moderatorOf.append(data)

def Map(sub):
	subreddit = None
	try:
		subreddit = reddit.get_subreddit(sub)
		mods = subreddit.get_moderators()
	except:
		print('Not a valid subreddit')
		return
	i=0
	fails=0
	for mod in mods:
		i = i+1
		print("\t" + str(i) + '/' + str(len(mods)) + ':\t' + mod.name, end='\t\t\t\t\r')
		pageRequest = url.Request('https://www.reddit.com/u/' + mod.name, headers = {'User-agent': 'ModMapper'})
		try:
			page = url.urlopen(pageRequest).read().decode("utf-8")
			scraper = ModListScraper()
			scraper.feed(page)
			for sub in scraper.moderatorOf:
				if (sub not in displayedSubs):
					displayedSubs.append(sub.lower())
					count.append([mod])
				else:
					count[displayedSubs.index(sub)].append(mod)
		except:
			fails = fails + 1

	print("\tScraped " + str(i - fails) + "/" + str(i) + " mods successfully!\t\t", end = '\n')

	i = 0
	for sub in displayedSubs:
		if(len(count[i]) >= minDisplay):
			string = "\t" + sub.ljust(25) + ": " + str(len(count[i])).rjust(2) 
			print(string) 
		i = i+1


displayedSubs = []
count = []
minDisplay = 2

reddit = praw.Reddit(user_agent='ModMapper')

print("Welcome to ModMapper!")
print("'quit' to exit")
print("'map [subreddit]' to map a subreddit")
print("'info [subreddit]' after mapping to see which mods overlap")
print("'minDisplay [number]' set the lowest number of overlap to display")
enter = None
while (enter != "quit"):
	enter = input("> ").lower()
	if(enter.startswith('info ')):
		enter = enter[5:]
		for mod in count[displayedSubs.index(enter)]:
			print("\t" + mod.name)
	elif(enter.startswith('map ')):
		enter = enter[4:]
		displayedSubs = []
		count = []
		Map(enter)
	elif(enter.startswith('mindisplay ')):
		enter = enter[11:]
		try:
			minDisplay = int(enter)
		except:
			print("Not a number")
		print("\tminDisplay set to " + str(minDisplay))



