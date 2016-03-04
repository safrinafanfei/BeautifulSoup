import urllib
from BeautifulSoup import *

url = raw_input('Enter URL- ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = raw_input('Enter count-')
position = raw_input('Enter position-')

# Retrieve all of the anchor tags
k = 1
while k <= count:
	tags = soup('a')	
	print "Retrieving: " + str(tags[int(position)-1])
	html = urllib.urlopen(tags[int(position)-1].get('href',None)).read()
	k += 1

		 	
	 
	    