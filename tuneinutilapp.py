#http://docs.python-guide.org/en/latest/scenarios/scrape/
#maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

from lxml import html
import requests
class TuneInUtilApp():
    @classmethod
    def go(cls):
        URL_BASE = 'https://tunein.com/radio/{}/'
        URL_PERU = 'Peru-r101285'
        page = requests.get(URL_BASE.format(URL_PERU))
        tree = html.fromstring(page.content)
        return tree
