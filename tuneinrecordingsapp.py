# http://docs.python-guide.org/en/latest/scenarios/scrape/
# maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages


OUTPUT_FILENAME = "thumbnails.html"
import os
import glob


#If I figure out a templating system, this would belong there.
IMAGE_FILE_AS_IMG_HTML = """
                <h1 style="font-family: quarca, helvetica, arial, sans-serif;">{image_filename}</h1>
                <img src="{image_filename}" 
                    alt="Image named {image_filename}" style="width: 150px;"/>
                """

BASE_DIR = 'tests/testbed/recordings'
class TuneInRecordingsApp():

    def __init__(self):
        pass
    @classmethod
    def pathed_image_filenames_in(cls, base_dir):
        image_files = []
        for directory in glob.glob(os.path.join(base_dir, "*")):
            for image in glob.glob(os.path.join(directory, "*.image")):
                image_files.append(image)
        return image_files

    def go(self, directory=BASE_DIR):
        image_files = self.__class__.pathed_image_filenames_in(directory)

        with open(OUTPUT_FILENAME, "w") as f:
            self.__class__.write_image_filenames_to(image_files, f)

    @classmethod
    def write_image_filenames_to(cls, image_files, output_file):
        output_file.write("<body>")

        for i in image_files:
            output_file.write(IMAGE_FILE_AS_IMG_HTML.format(image_filename=i))
        output_file.write("</body>")
