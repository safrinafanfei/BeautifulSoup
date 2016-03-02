from bs4 import BeautifulSoup as bs
import urllib

url="http://python-data.dr-chuck.net/comments_42.html"

soup = bs(urllib.urlopen(url))
for link in soup.findAll('span'):
        print link.string