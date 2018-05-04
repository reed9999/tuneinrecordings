import os
import glob
from behave import fixture, use_fixture
from hamcrest import assert_that, equal_to
from lxml import html
from shutil import copyfile, copy2, copytree, rmtree

from tuneinrecordingsapp import TuneInRecordingsApp as App

use_step_matcher("re")

#Wait to refactor until the tests all pass
# TESTCASES_SRC1 = [   #Start externalizing the lazy way, but eventually the DRY way...
#     '{}/1521309364.52960/e56200f5bbfbca547aa0712a5c9947aa.image',
#     '{}/1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image',
#     '{}/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image',
#     '{}/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image',
# ]

@given("There are no lingering output files")
def step_impl(context):
    if os.path.isfile("./thumbnails.html"):
        # os.remove("./thumbnails.html")
        pass
    dir = "tests/testbed/recordings"
    if os.path.isfile(dir + "/thumbnails.html"):
        # os.remove(dir + "/thumbnails.html")
        pass

@given("Individual recordings are present in (?P<testbed>[^ ]*)")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    testbed = "tests/testbed"
    dst = os.path.join(testbed, "recordings")
    store = os.path.join(testbed, "__store/recordings")
    for fn in glob.glob(pathname=os.path.join(store, "15*")):
        dst_file = os.path.join(dst, os.path.basename(fn))
        try:
            rmtree(dst_file)
        except FileNotFoundError:
            print("{} DNE".format(dst_file))
        except:
            raise
        copytree(fn, dst_file)


@given("Subdirs with recordings are present in (?P<testbed>[^ ]*)")
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


@step("I run the app")
def step_impl(context):
    """
    :type context: behave.runner.Context

    Step (which should probably really be a conventional unit test instead) to run the app
    without any parameter.
    """
    app = context.app = App()
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

@then("I get an HTML file (?P<output_file>.*) with img and alt for all thumbnails in (?P<testbed>[^ .]*)\.?")
def step_impl(context, output_file, testbed):
    """
    :type context: behave.runner.Context
    """

    assert os.path.isfile(output_file)
    assert os.path.isdir(testbed)
    with open(output_file, 'r') as f:
        img_dicts = all_imgs_in(f)
        img_srcs = [i['src'] for i in img_dicts]
        img_alts = [i['alt'] for i in img_dicts]
        assert_all_items_in(
            [   '{}/1521309364.52960/e56200f5bbfbca547aa0712a5c9947aa.image'.format(testbed),
                '{}/1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image'.format(testbed),
                '{}/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image'.format(testbed),
                '{}/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image'.format(testbed),
            ], img_srcs)
        assert 'Image named {}/1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image'.format(testbed) in img_alts

@then("I get an HTML file (?P<output_file>.*) with img and alt for all thumbnails in (?P<testbed>.*) and subdirs\.?")
def step_impl(context, output_file, testbed):
    """
    :type context: behave.runner.Context
    """
    #TODO possibly REFACTOR
    assert os.path.isfile(output_file)
    assert os.path.isdir(testbed)
    with open(output_file, 'r') as f:
        img_dicts = all_imgs_in(f)
        img_srcs = [i['src'] for i in img_dicts]
        img_alts = [i['alt'] for i in img_dicts]
        assert_all_items_in(
            [   '{}/2018-03/03-16-to-31/1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image'.format(testbed),
                '{}/2018-03/03-16-to-31/1521323051.57557/8c80fe611653c24656cbfa8a00b16ad4.image'.format(testbed),
                '{}/2018-03/special/1522427391.42871/8c4c2db15c4d3ca851b2a58c971b2fce.image'.format(testbed),
            ], img_srcs)
        assert_all_items_in(
            ['Image named {}/2018-03/03-16-to-31/1521323051.57557/8c80fe611653c24656cbfa8a00b16ad4.image'.format(testbed)],
            img_alts)






### TODO: This is for troubleshooting because it doesn't seem to recognize the parametrized one.
@step("Everything is set up in tests/testbed/another-path and subdirs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
