from behave import *
from tuneinrecordingsapp import TuneInRecordingsApp as App

use_step_matcher("re")

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

@when("I pass in the name (?P<testbed>[^ ]*)")
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
    pass


@then("I get an HTML file allowing me to view all thumbnails in (?P<testbed>[^ ]*) and subdirs\.?")
def step_impl(context, testbed):
    """
    :type context: behave.runner.Context
    """
    pass

