import os
from unittest import TestCase
from shutil import copytree, rmtree
from tuneinrecordingsapp import TuneInRecordingsApp as App

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
            path = "testbed/recordings/simple/{}".format(i)
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
        testbed = "testbed/recordings"
        src = os.path.join(testbed, "2018-03/03-16-to-31/1521620928.1166")
        dst = os.path.join(testbed, "simple/01")
        copytree(src=src, dst=dst)

        src = os.path.join(testbed, "2018-03/03-01-to-15")
        dst = os.path.join(testbed, "simple/02")
        copytree(src=src, dst=dst)

    def test_pathed_image_filenames_in(self):
        self.set_up_simple_filenames()
        bases = ["testbed/recordings/simple{}".format(i) for i in range(1, 3)]
        for base in bases:
            actual = App.pathed_image_filenames_in(base_dir=base, recursive=True)
            assert len(actual) > 0, "No image files in {}".base
            #Somehow I completely lost sight of what I'm trying to do here.
            #Iterate through the bases. For each base, there will be a different set of paths to
            # look for.
            for i in ["testbed/recordings/simple{}/xyzFAIL".format(j) for j in range(1, 3)]:
                if base == "testbed/recordings/2018-03":
                    assert i in actual, "Could not find {}".format(i)

    def test_go_no_params(self):
        for (k, app) in self._apps.items():
            app.go()
        self.skipTest("NYI")

    def test_go_does_not_raise_an_exception(self):
        for (k, app) in self._apps.items():
            try:
                app.go()
            except exception as e:
                self.fail("method go() of App constructed with {} raised {}!".format(k, e))

    def test_write_image_filenames_to(self):
        for (k, app) in self._apps.items():
            assert True, "failure in {}".format(k)
        self.skipTest("NYI")
