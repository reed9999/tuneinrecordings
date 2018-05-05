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

DEFAULT_BASE_DIR = 'tests/testbed/recordings'
DEFAULT_OUTPUT_FILE = './thumbnails.html'
class TuneInRecordingsApp():

    def __init__(self, base_dir=None, output_file=None):
        self._base_dir = (base_dir or DEFAULT_BASE_DIR)
        self._output_file = (output_file or DEFAULT_OUTPUT_FILE)

    @classmethod
    def pathed_image_filenames_in(cls, base_dir, recursive=True):
        if recursive == False:
            raise RuntimeError("Not yet implemented: Non-recursive handling.")
        image_files = []
        for root, directories, files in os.walk(base_dir):
        # for directory in glob.glob(os.path.join(base_dir, "*")):
            for directory in directories:
                for image in glob.glob(os.path.join(root, directory, "*.image")):
                    image_files.append(image)
        return image_files

    def go(self, directory=None, output_file=None):
        directory = (directory or self._base_dir)
        output_file = (output_file or self._output_file)
        image_files = self.__class__.pathed_image_filenames_in(directory)

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as f:
            self.__class__.write_image_filenames_to(image_files, f)

    @classmethod
    def write_image_filenames_to(cls, image_files, output_file):
        output_file.write("<body>")

        for i in image_files:
            output_file.write(IMAGE_FILE_AS_IMG_HTML.format(image_filename=i))
        output_file.write("</body>")
