import requests
from lxml import html

page = requests.get('https://www.craigslist.org/about/sites')
tree = html.fromstring(page.content)
hrefs = tree.xpath('//a')

print(hrefs)
