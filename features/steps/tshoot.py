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
    rv.append("""****LS PATH {}\n""".format(path))
    for (root, dn, fn) in os.walk(path):
        # print("root {} dn {} fn {}".format(root, dn, fn))
        rv.append("""LS STEP root {}\n""".format(root))
        rv.append("""LS STEP directory {} """.format(dn))
        rv.append("""LS STEP filename {} """.format(fn))
    context.tshoot_ls_info['ls step'] = rv
    print(context.tshoot_ls_info)
    assert len(rv), "ARRGH. directory {} should not be empty.\ntshoot info:\n{}".format(path, context.tshoot_ls_info)

@then(u'fail')
def step_impl(context):
    assert False, "tshoot info: \n{}".format(context.tshoot_ls_info)


@when(u'tshoot')
def step_impl(context):
    context.scenario.skip()
    path = os.path.join(THIS_FILE_DIR, '..', '..', 'tests', 'testbed-working')
    print("Eventually maybe run the app here or something")
    for (root, dn, fn) in os.walk(path):
        print("root {} dn {} fn {}".format(root, dn, fn))

