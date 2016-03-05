import urllib
import xml.etree.ElementTree as ET


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = urllib.urlopen(address).read()
    print 'Retrieving', url
    print 'Retrieved',len(url),'characters'
    print url
    tree = ET.fromstring(url)
    results = tree.findall('count').text
    print results

