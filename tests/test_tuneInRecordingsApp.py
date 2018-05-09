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
        bases = ["testbed/recordings"]
        bases.append(os.path.join(bases[0], "2018-03"))
        for base in bases:
            actual = App.pathed_image_filenames_in(base_dir=base, recursive=True)
            assert len(actual) > 0, "No image files in {}".base
            #Somehow I completely lost sight of what I'm trying to do here.
            #Iterate through the bases. For each base, there will be a different set of paths to
            # look for.
            for i in ['testbed/recordings/2018-03/03-16-to-31/1513103473.83708/abb7079cd48a474f19516e41fe5cdddd.image', 'testbed/recordings/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image', 'testbed/recordings/1521323051.57557/8c80fe611653c24656cbfa8a00b16ad4.image', 'testbed/recordings/1513103493.52414/abb7079cd48a474f19516e41fe5cdddd.image', 'testbed/recordings/1521309364.52960/e56200f5bbfbca547aa0712a5c9947aa.image', 'testbed/recordings/1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image', 'testbed/recordings/1521320898.1627/8c80fe611653c24656cbfa8a00b16ad4.image', 'testbed/recordings/1513213966.98665/abb7079cd48a474f19516e41fe5cdddd.image', 'testbed/recordings/2018-03/03-01-to-15/1520214773.17782/885cecbcd2adde480d030472cc9f5270.image', 'testbed/recordings/2018-03/03-01-to-15/1520966380.78764/cc763141baa8943f65cb69e5df7bcc76.image', 'testbed/recordings/2018-03/03-01-to-15/1520662680.71338/abb7079cd48a474f19516e41fe5cdddd.image', 'testbed/recordings/2018-03/03-01-to-15/1520484191.14983/d8108a021267bbefbd6276e35f7e8e3f.image', 'testbed/recordings/2018-03/03-01-to-15/1520484191.14983/842c160cc85594e74ae66bd12a391c90.image', 'testbed/recordings/2018-03/03-01-to-15/1520484191.14983/0e4943d31295954a7c730fa676567a05.image', 'testbed/recordings/2018-03/03-01-to-15/1520582381.12258/61bf1f5f280d21ad4b982c3083344740.image', 'testbed/recordings/2018-03/03-01-to-15/1520901307.12381/e647c8f5ba7a19cecd2e7381f11cec2c.image', 'testbed/recordings/2018-03/03-01-to-15/1520901307.12381/702ea3997ff54650d7ed07eb50a504fc.image', 'testbed/recordings/2018-03/03-01-to-15/1520666172.42772/abb7079cd48a474f19516e41fe5cdddd.image', 'testbed/recordings/2018-03/03-01-to-15/1520043840.34574/2beef8d2af2c8d22c9af3e349c8fe480.image', 'testbed/recordings/2018-03/03-01-to-15/1520043840.34574/25fc9b6f83187aaa75b93c7ed4c21c72.image', 'testbed/recordings/2018-03/03-01-to-15/1520782589.49738/4dbd88d99a66649272d482db6e6e5dfa.image', 'testbed/recordings/2018-03/03-01-to-15/1520782589.49738/7b9814e218e1d1839708b4fe50fb63c2.image', 'testbed/recordings/2018-03/03-01-to-15/1520782589.49738/efc770aa967efbacb2d978d350acca4c.image', 'testbed/recordings/2018-03/03-01-to-15/1520532800.1358/d8108a021267bbefbd6276e35f7e8e3f.image', 'testbed/recordings/2018-03/03-01-to-15/1520532800.1358/842c160cc85594e74ae66bd12a391c90.image', 'testbed/recordings/2018-03/03-01-to-15/1520064984.51562/25fc9b6f83187aaa75b93c7ed4c21c72.image', 'testbed/recordings/2018-03/03-01-to-15/1520895212.18060/702ea3997ff54650d7ed07eb50a504fc.image', 'testbed/recordings/2018-03/03-01-to-15/1520590761.93832/fe99ffe7b4db27f89ce80df262edc85d.image', 'testbed/recordings/2018-03/03-01-to-15/1520038897.68668/e6d5da8954b3dfbcd04124ad97ee52b7.image', 'testbed/recordings/2018-03/03-01-to-15/1520577842.24531/61bf1f5f280d21ad4b982c3083344740.image', 'testbed/recordings/2018-03/03-01-to-15/1520782024.53602/33f4cc851f6d3cd1fc8e0a86444874e4.image', 'testbed/recordings/2018-03/03-01-to-15/1520782024.53602/4dbd88d99a66649272d482db6e6e5dfa.image', 'testbed/recordings/2018-03/03-01-to-15/1520782024.53602/7b9814e218e1d1839708b4fe50fb63c2.image', 'testbed/recordings/2018-03/03-01-to-15/1520782024.53602/5d27166ad0b8ea357c7d92b37de4a8fe.image', 'testbed/recordings/2018-03/03-01-to-15/1520782024.53602/efc770aa967efbacb2d978d350acca4c.image', 'testbed/recordings/2018-03/03-01-to-15/1520902009.73840/e647c8f5ba7a19cecd2e7381f11cec2c.image', 'testbed/recordings/2018-03/03-01-to-15/1520902009.73840/702ea3997ff54650d7ed07eb50a504fc.image', 'testbed/recordings/2018-03/03-01-to-15/1520112079.19839/715615633c1e99161a2f2acb121bc4f1.image', 'testbed/recordings/2018-03/03-01-to-15/1520112079.19839/94e35589dae1c07730cf9ea86691c01d.image', 'testbed/recordings/2018-03/03-01-to-15/1520449180.73156/d653e80d348111747064512db29b13b6.image', 'testbed/recordings/2018-03/03-01-to-15/1520044440.1418/2beef8d2af2c8d22c9af3e349c8fe480.image', 'testbed/recordings/2018-03/03-01-to-15/1520044440.1418/25fc9b6f83187aaa75b93c7ed4c21c72.image', 'testbed/recordings/2018-03/03-16-to-31/1521620928.1166/7ad0c9958c6d293464354055df8f86b2.image', 'testbed/recordings/2018-03/03-16-to-31/1521574666.75599/87fea3e0ee79e243b360804a9f77ef60.image', 'testbed/recordings/2018-03/03-16-to-31/1521574666.75599/25fc9b6f83187aaa75b93c7ed4c21c72.image', 'testbed/recordings/2018-03/03-16-to-31/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image', 'testbed/recordings/2018-03/03-16-to-31/1521323051.57557/8c80fe611653c24656cbfa8a00b16ad4.image', 'testbed/recordings/2018-03/03-16-to-31/1521615636.96496/c541248ffe3dc6720b30d2af81a0b5c9.image', 'testbed/recordings/2018-03/03-16-to-31/1521309364.52960/e56200f5bbfbca547aa0712a5c9947aa.image', 'testbed/recordings/2018-03/03-16-to-31/1521257219.90161/a5ad95a922f9d44599c5bf73c8e1ae5b.image', 'testbed/recordings/2018-03/03-16-to-31/1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image', 'testbed/recordings/2018-03/03-16-to-31/1521320898.1627/8c80fe611653c24656cbfa8a00b16ad4.image', 'testbed/recordings/2018-03/03-16-to-31/1521642007.94387/84eb3121d25a77885290d5833fd75235.image', 'testbed/recordings/2018-03/03-16-to-31/1521603626.28095-HUGE/c541248ffe3dc6720b30d2af81a0b5c9.image', 'testbed/recordings/2018-03/03-16-to-31/1521574336.39118/abb7079cd48a474f19516e41fe5cdddd.image', 'testbed/recordings/2018-03/special/1522427391.42871/8c4c2db15c4d3ca851b2a58c971b2fce.image', 'testbed/recordings/special/1522427391.42871/8c4c2db15c4d3ca851b2a58c971b2fce.image']:
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
