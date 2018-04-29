#http://docs.python-guide.org/en/latest/scenarios/scrape/
#maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

from lxml import html
import requests
class TuneInRecordingsApp():

    def __init__(self):
        pass

    def go(self):
        BASE_DIR = 'tests/testbed/recordings'

