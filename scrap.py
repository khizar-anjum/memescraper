import urllib
import re
import subprocess
import time
import sys
from auth_file import reddit
import prawcore

urls="https://old.reddit.com/r/dankmemes/"

i=0
num = input("How many memes would you like to download?")
subReddit = reddit.subreddit('dankmemes');
if num<1:
	sys.exit("Number of pages should be > 0")
else :
	while i<num:
		current_timestamp = time.time()
		# 60 seconds * 60 minutes * 24 hours * 20 days = 20 days
		prev_timestamp = current_timestamp - (60 * 60 * 1 * 1)
		query = 'timestamp:{}..{}'.format(current_timestamp, prev_timestamp)+'&force_search_stack=cloudsearch'
		results = reddit.subreddit('dankmemes').search(query)
		try: 
			for submission in results:
				com = "wget " + submission.url + " --no-check-certificate -O " + submission.title + ".jpg";
				subprocess.call(com,shell=True)
			i+=60
		except prawcore.exceptions.ServerError as e:
			lastexception = e;
			print 'exception occured: ' + str(e)
			time.sleep(15);
		


    



