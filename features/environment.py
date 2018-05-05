import os
from behave import fixture, use_fixture
from tuneinrecordingsapp import TuneInRecordingsApp as App


@fixture
def app(context):
    # -- SETUP-FIXTURE PART:
    context.app = App()
    yield context.app
    # -- CLEANUP-FIXTURE PART: --- can I modify this comment at will?


def before_all(context):
    #use_fixture(app, context)
    #better to use a fixture....
    # make_testbed_writeable() #refactored for the moment
    pass

def before_tag(context, tag):
    if tag == "fixture.app":
        use_fixture(app, context)

def after_all(context):
    pass
