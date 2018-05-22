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
def skip(context):
    context.scenario.skip()

def all_img_attributes_in(f):
    img_dicts = all_imgs_in(f)
    img_srcs = [i['src'] for i in img_dicts]
    img_alts = [i['alt'] for i in img_dicts]
    return img_srcs, img_alts

def all_imgs_in(the_file):
    """
    :returns dict of the src and alt attributes for all img tags in the file given
    This is a helper for tests that verify img tags are as expected in the file.
    """
    tree = html.fromstring(the_file.read())
    xpath = '//img'
    all_attributes_as_2d_list = [x.items() for x in tree.xpath(xpath)]

    #There should be a way to keep doing this with nested comprehensions
    # although I'm not sure it's worth sacrificing readability for Pythonicity
    rv = []
    for one_list_of_attributes in all_attributes_as_2d_list:
        #Does Python have an equivalent to ruby's "select" on a list?
        src = [v for (k, v) in one_list_of_attributes if k == 'src'][0]
        alt = [v for (k, v) in one_list_of_attributes if k == 'alt'][0]
        rv.append({'src': src, 'alt': alt})
    return rv

def assert_all_items_in(list_of_expected, actual_list):
    for item in list_of_expected:
        assert item in actual_list, "Not in the list of actuals: {}".format(item)

def assert_all_img_and_alt_present(output_file, testbed, recursive=True):
    with open(output_file, 'r') as f:
        img_srcs, img_alts = all_img_attributes_in(f)
        expected = TEST_RESULTS['all_imgs']

        base = os.path.abspath(".")
        full_list_of_absolute_src_paths = \
            [os.path.join(base, x.format(testbed)) for x in expected]
        assert_all_items_in(full_list_of_absolute_src_paths, img_srcs)
        assert_all_items_in(["Image named {}".format(x) for x in full_list_of_absolute_src_paths], img_alts)
    if not recursive:
        raise NotImplementedError


@given("[Tt]here are no lingering output files")
def step_impl(context):
    default_output = PATHS['default']['output']
    if os.path.isfile(default_output):
        os.remove(default_output)
    #some other places I've been leaving clutter.
    fn = os.path.join(THIS_FILE_DIR, '..', 'recordings', 'thumbnails.html')
    if os.path.isfile(fn):
        os.remove(fn)

@given("individual recordings are present in (?P<input_place>.*) place")
def step_impl(context, input_place):
    """
    Checks the setup to make sure files are ready for processing.

    Eventually I may want to refactor the default place vs. arbitrary place
    functionality into two different functions. Later.

    :type context: behave.runner.Context
    """
    store = PATHS['store']
    dst = PATHS['default']['input']
    for fn in glob.glob(pathname=os.path.join(store, "15*")):
        dst_file = os.path.join(dst, os.path.basename(fn))
        try:
            rmtree(dst_file)
        except FileNotFoundError:
            pass
        except:
            raise
        copytree(fn, dst_file)


@given("XXX")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """

    testbed = "tests/testbed"
    dst = os.path.join(testbed, "recordings/2018-03")
    store = os.path.join(testbed, "__store/recordings/2018-03")
    try:
        rmtree(dst)
    except FileNotFoundError:
        print("{} DNE".format(dst))
    except:
        raise
    copytree(store, dst)


@when("I run the app")
def step_impl(context):
    """
    :type context: behave.runner.Context

    Step (which should probably really be a conventional unit test instead) to run the app
    without any parameter.
    """
    app = context.app
    app.go()

@when("I run the app passing in the name (?P<testbed>[^ ]*)")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context

    Step (which should probably really be a conventional unit test instead) to run the app
    with a stated parameter.
    """
    #context.testbed = testbed
    context.scenario.skip()

@then("I get an HTML output file in (?P<output_place>.*) output place")
def step_impl(context, output_place):
    """
    :type context: behave.runner.Context
    """
    if not re.search('default', output_place):
        context.scenario.skip()
        print("NYI: Must use the default place right now.")
        return
    output_file = PATHS['default']['output']
    assert os.path.isdir(os.path.dirname(output_file))
    context.output_file = output_file


@then("the output file displays images for img tags in (?P<input_place>.*) place and subdirs\.?")
def step_impl(context, input_place):
    """
    :type context: behave.runner.Context
    """
    #recursive=False doesn't do anything yet
    try:
        #Does this make sense? Why is the test doing its own analysis instead
        # of reading an oracle?
        # assert_all_img_and_alt_present(output_file=output_file,
        #                    testbed=PATHS['default']['input'], recursive=False)
        with open(context.output_file, 'r') as f:
            html = f.read()
            for img in TEST_RESULTS['all_imgs']:
                msg = "ASSERT FAIL: img={img}, html={html}, search={search}".format(
                    img=img, html=html, search=search,
                )
                assert re.search(img.replace('/','.'), html), msg
    except NotImplementedError:
        msg = "Non-recursive behavior is not yet/might never be implemented."
        print("WARNING: " + msg)

@then(u'I get an HTML file (?P<output_file>.*) with img and alt for all thumbnails in (?P<testbed>.*) and subdirs\.?')
def step_impl(context, output_file, testbed):
    """
    :type context: behave.runner.Context
    """
    assert os.path.isfile(output_file), "File {} does not exist".format(output_file)
    assert os.path.isdir(testbed), "Dir {} does not exist".format(testbed)
    assert_all_img_and_alt_present(output_file=output_file,
                                           testbed=testbed, recursive=True)




@when("I run the app with output file (?P<output_file>.*)")
def step_impl(context, output_file):
    """
    :type context: behave.runner.Context
    """
    context.app.go(output_file=output_file)


#NOT YET IMPLEMENTED STUFF

@given("the GUI is running")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when("I invoke the image naming dialogue")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@step("I use the GUI to assign names to images")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@then("the names I assigned are retained\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    skip(context)

#HARD CODED FOR NOW, need to be made parametrized.
@then(u'the output file gives directory locations for images displayed')
def step_impl(context):
    """
    This is a really hard one to implement because I need to not just match the
    img file name but also make sure the directory part is displayed.
    Perhaps the best thing is to walk through the HTML and use a suitable
    xpath?
    :param context:
    :return:
    """
    raise NotImplementedError(u'STEP: Then the output file gives directory locations for images displayed')

@then(u'the images have alt tags for all alt tags in the default place and subdirs.')
def step_impl(context):
    """
    As with the previous one, hard to implement because I need to not just
    match the img file name but also make sure the directory part is displayed.
    Perhaps the best thing is to walk through the HTML and use a suitable
    xpath?
    :param context:
    :return:
    """
    raise NotImplementedError(u'STEP: Then the images have alt tags for all alt tags in the default place and subdirs.')

