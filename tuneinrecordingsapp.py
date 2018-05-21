# http://docs.python-guide.org/en/latest/scenarios/scrape/
# maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages


import os
import glob
import django.template
from django.conf import settings
settings.configure(TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.'],
        'APP_DIRS': False,

    },
]
)
django.setup()

THIS_FILE_DIR = os.path.dirname(__file__)
DEFAULT_OUTPUT_FILE = os.path.join(THIS_FILE_DIR, 'thumbnails.html')
# If I figure out a templating system, this would belong there.
IMAGE_FILE_AS_IMG_HTML = """
                <h1 style="font-family: quarca, helvetica, arial, sans-serif;">{image_filename}</h1>
                <img src="{image_filename}" 
                    alt="Image named {image_filename}" style="width: 150px;"/>
                """

PROJECT_ROOT_DIR = os.path.dirname(__file__)
#TODO!
# Why on earth is the app defaulting to the testbed anyway???
# It's nice to make tests pass, but the app shouldn't know about the testbed!
# Figure out a better way to handle this default.
DEFAULT_BASE_DIR = os.path.join(PROJECT_ROOT_DIR, 'tests', 'testbed-working', 'recordings')


class TuneInRecordingsApp():
    """
    Main application class to help manage numerous TuneIn recordings.

    This whole project is an exercise in overdesign, of course. That's how I
    learn.

    At present the command line interface isn't yet implemented.
    >>> from tuneinrecordingsapp import TuneInRecordingsApp as App
    >>> App().go()


    """

    def __init__(self, base_dir=None, output_file=None):
        self._base_dir = (base_dir or DEFAULT_BASE_DIR)
        self._output_file = (output_file or DEFAULT_OUTPUT_FILE)

    @classmethod
    def pathed_image_filenames_in(cls, base_dir, recursive=True):
        if recursive == False:
            raise RuntimeError("Not yet implemented: Non-recursive handling.")
        image_files = []
        for root, directories, files in os.walk(base_dir):
            for directory in [''] + directories:
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
    def new_django_template(cls, image_files, output_file):
        t = django.template.Template("{{image_files.0}}")
        c = django.template.Context({'image_files': image_files})
        print(t.render(c))
        return (t.render(c))

    @classmethod
    def write_image_filenames_to(cls, image_files, output_file):

        output_file.write("<body>")
        for i in image_files:
            output_file.write(IMAGE_FILE_AS_IMG_HTML.format(image_filename=os.path.abspath(i)))
        output_file.write("</body>")
        #demo for now
        _ = cls.new_django_template(image_files, output_file)
