import os
from behave import *
from tuneinrecordingsapp import TuneInRecordingsApp as App
from lxml import html

use_step_matcher("re")

@fixture
def app():
    print ("I should set up the app")

@when("Everything is set up in (?P<testbed>[^ ]*)")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    pass

@when("Everything is set up in (?P<testbed>[^ ]*) and subdirs")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    pass

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
    pass


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

@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*)\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    assert os.path.isfile(os.path.join(testbed, "thumbnails.html"))
    with open(os.path.join(testbed, "thumbnails.html"), 'r') as f:
        img_dicts = all_imgs_in(f)
        img_srcs = [i['src'] for i in img_dicts]
        img_alts = [i['alt'] for i in img_dicts]
        assert_all_items_in(
            [   '1521309364.52960/e56200f5bbfbca547aa0712a5c9947aa.image',
                '1521320898.1627/60a58df0b9d06ce905b72c371a665d93.image',
                '1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image',
                '1521323051.57557/60a58df0b9d06ce905b72c371a665d93.image',
            ], img_srcs)
        assert 'Image for recording 1521320898.1627' in img_alts


@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*) and subdirs\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """


