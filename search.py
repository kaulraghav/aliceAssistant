from google import search
import urllib
from bs4 import BeautifulSoup
import webbrowser
import pyperclip
def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

i = 1
query=pyperclip.paste()

for url in search(query, stop=10):
    a = google_scrape(url)
    print str(i) + ". " + a
    print url
    webbrowser.open(url)
    i += 1