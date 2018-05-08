import os
from unittest import TestCase
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

    def construct_no_params(self):
        return App()

    def construct_base_dir_only(self, bd):
        return App(base_dir=bd, output_file=None)

    def construct_output_file_only(self, of):
        return App(base_dir=None, output_file=of)

    def construct_both_params(self, base_dir, output_file):
        return App(base_dir=base_dir, output_file=output_file)

    def test_pathed_image_filenames_in(self):
        for (k, v) in self._apps.items():
            assert False, "failure in {}".format(k)

    def test_go(self):
        self.skipTest("NYI")

    def test_write_image_filenames_to(self):
        self.skipTest("NYI")
