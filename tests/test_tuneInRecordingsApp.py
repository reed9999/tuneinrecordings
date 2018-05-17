import os
from unittest import TestCase
from shutil import copytree, rmtree
from lxml import html
from tuneinrecordingsapp import TuneInRecordingsApp as App
from .results import TEST_RESULTS


TESTBED_PATH = 'tests/testbed'
TEST_PATHS = {
    'base1': os.path.join(TESTBED_PATH, 'base1'),
    'base2': os.path.join(TESTBED_PATH, 'base2'),
    'output1': os.path.join(TESTBED_PATH, 'output1'),
    'output2': os.path.join(TESTBED_PATH, 'output2'),
}
class TestTuneInRecordingsApp(TestCase):
    def setUp(self):
        T = TEST_PATHS
        #Perhaps this should be one-time or lazy setup; as is, it's
        # inefficient to keep creating apps we don't use.
        self._apps = {
            'no params': self.construct_no_params(),
            'base only': self.construct_base_dir_only(T['base1']),
            'output only': self.construct_output_file_only(T['output1']),
            'both': self.construct_both_params(base_dir=T['base2'],
                                               output_file=T['output2']),
        }
        self.rm_old_contents()

    def rm_old_contents(self):
        for i in range(1, 3):
            path = "testbed/recordings/simple/{0:02d}".format(i)
            if os.path.isdir(path):
                rmtree(path)

    def construct_no_params(self):
        return App()

    def construct_base_dir_only(self, bd):
        return App(base_dir=bd, output_file=None)

    def construct_output_file_only(self, of):
        return App(base_dir=None, output_file=of)

    def construct_both_params(self, base_dir, output_file):
        return App(base_dir=base_dir, output_file=output_file)

    def set_up_simple_filenames(self):
        this_file_dir = os.path.dirname(__file__)
        testbed = os.path.join(this_file_dir,"testbed", "recordings")
        assert os.path.isdir(testbed)
        src = os.path.join(testbed, "2018-03/03-16-to-31/1521620928.1166")
        dst = os.path.join(testbed, "simple/01")
        copytree(src=src, dst=dst)

        src = os.path.join(testbed, "2018-03/03-01-to-15")
        dst = os.path.join(testbed, "simple/02")
        copytree(src=src, dst=dst)

    def test_pathed_image_filenames_in(self):
        self.set_up_simple_filenames()
        root_dir = os.path.join(os.path.dirname(__file__), "testbed",
                                "recordings", "simple")
        bases = [os.path.join(root_dir, "{0:02d}".format(i)) for i in range(1, 3)]
        for base in bases:
            actual = App.pathed_image_filenames_in(base_dir=base, recursive=True)
            assert len(actual) > 0, "No image files in {0}".format(base)
            #Somehow I completely lost sight of what I'm trying to do here.
            #Iterate through the bases. For each base, there will be a different set of paths to
            # look for.
            for i in ["testbed/recordings/simple{}/xyzFAIL".format(j) for j in range(1, 3)]:
                if base == "testbed/recordings/2018-03":
                    assert i in actual, "Could not find {}".format(i)

    def generic_test_go(self, app):
        app.go()
        self.verify_all_expected_contents(app)

    # I can't decide if it's better to iterate through the four in one test
    # method or isolate each one like this. The advantage of this approach
    # is getting a clearly different test result for each within every
    # standard test runner UI.
    # There is probably some way to synthetically create test methods
    # (perhaps a lambda?).

    def test_go_no_params(self):
        self.generic_test_go(self._apps['no params'])

    def test_go_base_only(self):
        self.generic_test_go(self._apps['base only'])

    def test_go_output_only(self):
        self.generic_test_go(self._apps['output only'])

    def test_go_both(self):
        self.generic_test_go(self._apps['both'])

    def test_go_does_not_raise_an_exception(self):
        for (k, app) in self._apps.items():
            try:
                app.go()
            except Exception as e:
                msg = "method go() of App constructed with {} raised {}!"
                msg = msg.format(k, e)
                self.fail(msg)

    def test_write_image_filenames_to(self):
        for (k, app) in self._apps.items():
            assert True, "failure in {}".format(k)
        self.skipTest("NYI")

    def verify_all_expected_contents(self, app):
        self.assert_all_img_and_alt_present('./thumbnails.html', 'testbed')

    # See thumbnails.feature
    # Part of my dithering between what's a feature test and what's a unit test.
    # If I really do want to keep this both places, REFACTOR to make it a helper.
    # NOTE: Right now these are all instance methods that don't use any
    # instance variables. That's silly so I will want to REFACTOR that too
    # although should probably just wait to decide on a helper.
    def all_img_attributes_in(self, filename):
        img_dicts = self.all_imgs_in(filename)
        img_srcs = [i['src'] for i in img_dicts]
        img_alts = [i['alt'] for i in img_dicts]
        return img_srcs, img_alts

    def all_imgs_in(self, the_file):
        """
        :returns dict of the src and alt attributes for all img tags in the file given
        This is a helper for tests that verify img tags are as expected in the file.
        """
        tree = html.fromstring(the_file.read())
        xpath = '//img'
        all_attributes_as_2d_list = [x.items() for x in tree.xpath(xpath)]

        # There should be a way to keep doing this with nested comprehensions
        # although I'm not sure it's worth sacrificing readability for Pythonicity
        rv = []
        for one_list_of_attributes in all_attributes_as_2d_list:
            # Does Python have an equivalent to ruby's "select" on a list?
            src = [v for (k, v) in one_list_of_attributes if k == 'src'][0]
            alt = [v for (k, v) in one_list_of_attributes if k == 'alt'][0]
            rv.append({'src': src, 'alt': alt})
        return rv

    def assert_all_img_and_alt_present(self, output_file, testbed, recursive=True):
        with open(output_file, 'r') as f:
            img_srcs, img_alts = self.all_img_attributes_in(f)
            expected = TEST_RESULTS['all_imgs']

            base = os.path.abspath(".")
            full_list_of_absolute_src_paths = \
                [os.path.join(base, x.format(testbed)) for x in expected]
            self.assert_all_items_in(full_list_of_absolute_src_paths, img_srcs)
            self.assert_all_items_in(["Image named {}".format(x) for x in full_list_of_absolute_src_paths], img_alts)
        if not recursive:
            raise NotImplementedError

    def assert_all_items_in(self, list_of_expected, actual_list):
        for item in list_of_expected:
            assert item in actual_list, "Not in the list of actuals: {}".format(item)

