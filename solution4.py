import urllib
from BeautifulSoup import *

url = raw_input('Enter URL- ')
count = raw_input('Enter count-')
position = raw_input('Enter position-')

for i in range(int(count)):
	url = BeautifulSoup(urllib.urlopen(url).read())('a')[int(position) - 1].get('href', None)
	print url