#http://docs.python-guide.org/en/latest/scenarios/scrape/
#maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

from lxml import html
import requests
class TuneInUtilApp():

    def go(self):
        URL_BASE = 'https://tunein.com/radio/{}/'
        URL_PERU = 'Peru-r101285'
        page = requests.get(URL_BASE.format(URL_PERU))
        tree = self.tree = html.fromstring(page.content)
        #data-reactid's can work too but change on each execution.
        XPATH = GOOD_XPATH = '//div[@id="container-1"]//div'
        BAD_XPATH = '//div[@data-reactid="136"]/*/text()'
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

