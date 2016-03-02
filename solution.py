import urllib
from BeautifulSoup import *
url = raw_input('Enter-')
html = urllib.urlopen(url).read()
soup =BeautifulSoup(html)
# Retrieve all of the span tags
tags = soup('span')
sum = 0
for tag in tags:
	a = int(tag.contents[0])
	sum = sum + a
print sum