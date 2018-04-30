#http://docs.python-guide.org/en/latest/scenarios/scrape/
#maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

OUTPUT_FILENAME = "thumbnails.html"
import os
import django.template as dtl
import glob

class TuneInRecordingsApp():

    BASE_DIR = 'tests/testbed/recordings'
    def __init__(self):
        pass

    def go(self):
        BASE_DIR = self.__class__.BASE_DIR
        image_files = []
        for directory in glob.glob(os.path.join(BASE_DIR, "*")):
            for image in glob.glob(os.path.join(directory, "*.image")):
                image_files.append(image)

        with open(OUTPUT_FILENAME, "w") as f:
            #Eventually this should be templated, perhaps with Django templates.
            f.write("<body>")
            for i in image_files:
                f.write("""
                <h1>{}</h1>
                <img src="{}" 
                    alt="Image named {}" />
                    """.format(i, i, i))
            f.write("</body>")

