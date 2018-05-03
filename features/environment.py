import os
from behave import fixture, use_fixture
from tuneinrecordingsapp import TuneInRecordingsApp as App


@fixture
def app(context):
    # -- SETUP-FIXTURE PART:
    context.app = App()
    yield context.app
    # -- CLEANUP-FIXTURE PART: --- can I modify this comment at will?
    print("No shutdown needed")

def make_testbed_writeable():
    path = "tests/testbed"
    for root, dirs, files in os.walk(path):
        #https://stackoverflow.com/q/2853723/742573
        for d in dirs:
            os.chmod(os.path.join(root, d), 0o755)
        for f in files:
            os.chmod(os.path.join(root, f), 0o755)

def before_all(context):
    #use_fixture(app, context)
    #better to use a fixture....
    make_testbed_writeable()

def before_tag(context, tag):
    if tag == "app":
        use_fixture(app, context)

def after_all(context):
    pass
