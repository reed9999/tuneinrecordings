#http://docs.python-guide.org/en/latest/scenarios/scrape/
#maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

from lxml import html
import requests
class TuneInUtilApp():

    def __init__(self):
        self.country = None
    def set_country(self, new_country):
        self.country = new_country

    def go(self, country=None):
        URL_BASE = 'https://tunein.com/radio/{}/'

        #Messing with short-circuiting / lazy Boolean evaluation.
        # come back to this idea if it's considered Pythonic

        # if (self.country is None):
        #     print ("H")
        # country = self.country or country
        # assert self.country is not None

        assert country is not None
        self.country = country
        if country == 'Peru':
            country_url = 'Peru-r101285'
        if country == 'Myanmar':
            country_url = 'Myanmar-(Burma)-r100382'

        page = requests.get(URL_BASE.format(country_url))
        tree = self.tree = html.fromstring(page.content)
        #data-reactid's can work too but change on each execution.
        XPATH = GOOD_XPATH = '//div[@id="container-1"]//div'
        station_names = [node.text for node in tree.xpath(XPATH)]
        return (station_names)


        # XPATH = XPATH_containerGuideItemsContainer = '//div[@data-reactid="136"]/*/*/*/*'
        # XPATH_text = XPATH + "/text()"
        # print (tree.xpath(XPATH))
        # print (tree.xpath(XPATH_text))
        # return (tree.xpath(XPATH_text))
        #
    def inspect_tree(self):
        #'data-testid'=guideItemTitle
        pass

