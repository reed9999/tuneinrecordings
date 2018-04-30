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

    #There should be a nested-comprehension way to do this although I'm not
    # sure it's worth sacrificing readability for Pythonicity
    rv = []
    for one_list_of_attributes in all_attributes_as_2d_list:
        src = [v for (k, v) in one_list_of_attributes if k == 'src'][0]
        alt = [v for (k, v) in one_list_of_attributes if k == 'alt'][0]
        rv.append({'src': src, 'alt': alt})

    return rv


@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*)\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    assert os.path.isfile(os.path.join(testbed, "thumbnails.html"))
    with open(os.path.join(testbed, "thumbnails.html"), 'r') as f:
        img_dicts = all_imgs_in(f)
        img_srcs = [i['src'] for i in img_dicts]
        assert 'xyz' in img_srcs
        assert 'abc' in img_srcs


@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*) and subdirs\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """


