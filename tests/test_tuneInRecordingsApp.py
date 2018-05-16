import os
from unittest import TestCase
from shutil import copytree, rmtree
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

    #I can't decide if it's better to iterate through the four in one test
    #method or isolate each one like this.
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
        self.assert_output_contains_all_img_and_alt('./thumbnails.html', 'testbed')

    # See thumbnails.feature
    # Part of my dithering between what's a feature test and what's a unit test.
    # If I really do want to keep this both places, REFACTOR to make it a helper.
    def assert_output_contains_all_img_and_alt(self, output_file, testbed):
        self.skipTest("NYI")
