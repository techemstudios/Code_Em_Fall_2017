"""
Web scrape to get next week's recipe titles and descriptions from Blue Apron.

Example of retrieving data from a site, with no need of api key.

Pull html, parse it, handle it to return values that make sense.

Using Beautiful Soup
"""

from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.blueapron.com/pages/sample-recipes'

uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

recipes = page_soup.findAll("div",{"class":"tab-content js-initialMenu"})

for recipe in recipes:
    title = recipe.findAll("div", {"class":"recipe-title"}) #**
    title[0].encode("ascii")

for name in title:
    print(name.text)




