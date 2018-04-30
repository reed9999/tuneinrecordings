#http://docs.python-guide.org/en/latest/scenarios/scrape/
#maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

OUTPUT_FILENAME = "thumbnails.html"
import os
import django.template as dtl

class TuneInRecordingsApp():

    def __init__(self):
        pass

    def go(self):
        BASE_DIR = 'tests/testbed/recordings'
        with open(os.path.join(BASE_DIR, OUTPUT_FILENAME), "w") as f:
            f.write("0x00")

