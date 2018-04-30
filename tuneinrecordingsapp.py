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
            f.write("""
            <body>
            <h1>1521320898.1627</h1>
                <img src="1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image" 
                    alt="Image for recording 1521320898.1627" />
            <h1>1521323051.57557</h1>
                <img src="1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image" 
                    alt="Image for recording 1521323051.57557" />
                <img src="1521323051.57557/8c80fe611653c24656cbfa8a00b16ad4.image" 
                    alt="Image for recording 1521323051.57557" /> <!-- obv not unique alt -->
            </body>
            """)

