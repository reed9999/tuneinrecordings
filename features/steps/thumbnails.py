import os
from behave import *
from tuneinrecordingsapp import TuneInRecordingsApp as App

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


@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*)\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    assert os.path.isfile(os.path.join(testbed, "thumbnails.html"))
    with open(os.path.join(testbed, "thumbnails.html"), 'r') as f:
        assert f

@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*) and subdirs\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    context.scenario.skip()

