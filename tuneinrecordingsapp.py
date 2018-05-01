# http://docs.python-guide.org/en/latest/scenarios/scrape/
# maybe also #https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

OUTPUT_FILENAME = "thumbnails.html"
import os
import django.template as dtl
import glob

# This would be in the settings in a Django project. Not exactly sure how it fits in here....
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]

#And this is what should be moved there
IMAGE_FILE_AS_IMG_HTML = """
                <h1>{image_filename}</h1>
                <img src="{image_filename}" 
                    alt="Image named {image_filename}" />
                """

class TuneInRecordingsApp():
    BASE_DIR = 'tests/testbed/recordings'

    def __init__(self):
        pass

    def pathed_image_filenames_in(self, base_dir):
        image_files = []
        for directory in glob.glob(os.path.join(self.__class__.BASE_DIR, "*")):
            for image in glob.glob(os.path.join(directory, "*.image")):
                image_files.append(image)
        return image_files

    def go(self):
        image_files = self.pathed_image_filenames_in(self.__class__.BASE_DIR)

        with open(OUTPUT_FILENAME, "w") as f:
            self.__class__.write_image_filenames_to(image_files, f)
            # Eventually this should be templated, perhaps with Django templates.
            # f.write("<body>")
            # for i in image_files:
            #     f.write("""
            #     <h1>{}</h1>
            #     <img src="{}"
            #         alt="Image named {}" />
            #         """.format(i, i, i))
            # f.write("</body>")

    @classmethod
    def write_image_filenames_to(cls, image_files, output_file):
        output_file.write("<body>")


        for i in image_files:
            output_file.write(IMAGE_FILE_AS_IMG_HTML.format(image_filename=i))
        output_file.write("</body>")
