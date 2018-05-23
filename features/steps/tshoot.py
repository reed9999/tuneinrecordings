import os
import glob
import re
from tests.results import TEST_RESULTS
#from hamcrest import assert_that, equal_to
from lxml import html
from shutil import copyfile, copy2, copytree, rmtree

use_step_matcher("re")

THIS_FILE_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.join(THIS_FILE_DIR, '..', '..')
PATHS = {
    #Nested better than tuple approach, I can tell. Need to retrofit slightly.
    'default': {'input': os.path.join(PROJECT_ROOT, 'tests', 'testbed-working', 'recordings'),
        'output': os.path.join(PROJECT_ROOT, 'thumbnails.html')},
    ('output', 'default'): os.path.join(PROJECT_ROOT, 'tests', 'another-arbitrary-dir', 'arbitrary-filename.txt'),
    ('input', 'default'): os.path.join(PROJECT_ROOT, 'tests', 'testbed-working', 'recordings'),
    ('output', 'default'): os.path.join(PROJECT_ROOT, 'thumbnails.html'),
    ('input', 'arbitrary'): os.path.join(PROJECT_ROOT, 'tests', 'arbitrary-name'),
    ('output', 'default'): os.path.join(PROJECT_ROOT, 'tests', 'another-arbitrary-dir', 'arbitrary-filename.txt'),
    'store': os.path.join(PROJECT_ROOT, 'tests', 'testbed-store'),
}

@then(u'ls')
def step_impl(context):
    path = os.path.join(THIS_FILE_DIR, '..', '..', 'tests', 'testbed-working')
    rv = []
    for (root, dn, fn) in os.walk(path):
        # print("root {} dn {} fn {}".format(root, dn, fn))
        rv.append((root, dn, fn))
    context.tshoot = rv
    assert False, "Here is the tshoot info: \n{}".format(context.tshoot_ls_info)
    assert False, context.tshoot

@when(u'tshoot')
def step_impl(context):
    context.scenario.skip()
    path = os.path.join(THIS_FILE_DIR, '..', '..', 'tests', 'testbed-working')
    print("Eventually maybe run the app here or something")
    for (root, dn, fn) in os.walk(path):
        print("root {} dn {} fn {}".format(root, dn, fn))

