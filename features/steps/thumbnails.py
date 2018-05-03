import os
import glob
from behave import fixture, use_fixture
from hamcrest import assert_that, equal_to
from lxml import html
from shutil import copyfile, copy2, copytree, rmtree

from tuneinrecordingsapp import TuneInRecordingsApp as App

use_step_matcher("re")


@given("There are no lingering output files")
def step_impl(context):
    if os.path.isfile("./thumbnails.html"):
        os.remove("./thumbnails.html")
    dir = "tests/testbed/recordings"
    if os.path.isfile(dir + "/thumbnails.html"):
        os.remove(dir + "/thumbnails.html")

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
    print("Not skipping but not set up well")
    return

    path = "tests/testbed/recordings/2018-03"
    try:
        rmtree(path)
    except FileNotFoundError:
        print("{} DNE".format(path))
    except:
        raise
    # Failing on permissions -- somehow I've misorganized this.
    copytree("/home/philip/Music/Tunein/2018-03", "tests/testbed/recordings/2018-03")


@step("I run the app")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    app = context.app = App()
    app.go()

@when("I run the app passing in the name (?P<testbed>[^ ]*)")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    #context.testbed = testbed
    context.scenario.skip()

def all_imgs_in(the_file):
    """
    :returns dict
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

@then("I get an HTML file (?P<output_file>.*) allowing me to view all thumbnails in (?P<testbed>.*) and subdirs\.?")
def step_impl(context, output_file, testbed):
    """
    :type context: behave.runner.Context
    """
    context.scenario.skip()



#### Getting too meta, but a very in-my-face way to track my own knowledge gap.
@fixture
def arbitrary_fixture(context):
    # -- SETUP-FIXTURE PART:
    context.app_from_arbitrary_fixture = App()
    yield context.app_from_arbitrary_fixture
    # -- CLEANUP-FIXTURE <....>: --- can I modify this comment at will?
    del context.app_from_arbitrary_fixture
    print("Not much shutdown needed")


@when("I run a test with a fixture")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("The test should use the fixture\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass




# behave correctly recognizes as ambiguous. Why not the others?
# @then("I get an HTML file ./thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass

### TODO: Less parametrized, but it's for troubleshooting because it doesn't seem to recognize the parametrized one.
@step("Everything is set up in tests/testbed/another-path and subdirs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

# behave correctly recognizes as ambiguous. Why not the others?
# @when("I run the app passing in the name tests/testbed/another-path")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass