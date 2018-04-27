from behave import *
from tuneinutilapp import TuneInUtilApp as App

use_step_matcher("re")


@when("I pass in a language and (?P<kind_of_genre>.*) genre")
def step_impl(context, kind_of_genre):
    """
    :type context: behave.runner.Context
    """
    assert('music' == kind_of_genre)
    app = context.app = App()


@then("I get a convenient list of all stations matching both language and genre")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.scenario.skip("NYI")


@when("I pass in the country (?P<country_name>.*)")
def step_impl(context, country_name):
    """
    :type context: behave.runner.Context
    """
    app = context.app = App()
    context.country_name = country_name
    print(country_name)


@then("I get a convenient list of all stations from (?P<expected_country_name>.*)\.?")
def step_impl(context, expected_country_name):
    """
    :type context: behave.runner.Context
    """
    station_names = list(context.app.go())
    assert (station_names is not None)
    assert (len(station_names) > 1)  # Peru should have more than 1
    assert ('Radio Super Latina La Merced' in station_names)
    assert ('RADIO LA FUERTE' in station_names)
    print(type(station_names))  # assert(not None in station_names)
    print(station_names)
#    assert(the_html.attrib['lang'] == 'en-us')
