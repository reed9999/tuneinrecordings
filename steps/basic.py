from behave import *
from tuneinutilapp import TuneInUtilApp as App

use_step_matcher("re")


def expected_station_names_for(country):
    data = {
        'Peru': ['Radio Super Latina La Merced', 'RADIO LA FUERTE', 'Union La Radio'],
        'Myanmar': ['Mandalay FM', 'Padamyar FM', ],
        'Russia': ['Radio Super Latina La Merced', 'RADIO LA FUERTE', ],
            }
    return data[country]

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
    #TODO: Make this return value accessible from app; feels wrong to stash it here.
    context.actual_names = list(context.app.go(country_name))


@then("I get a convenient list of all stations from (?P<country_name>.*)\.?")
def step_impl(context, country_name):
    """
    :type context: behave.runner.Context
    """
    actual_names = context.actual_names
    assert country_name == context.country_name
    assert (actual_names is not None)
    assert (len(actual_names) > 1)  # countries in test should have > 1... maybe. (Reconsider.)
    print(actual_names)
    expected_names = expected_station_names_for(country_name)
    # *Doesn't work: assert ([(the_name in actual_names) for the_name in expected_names])
    for the_name in expected_names:
        assert the_name in actual_names, "Not present: {}".format(the_name)
        # assert (expected_names[0] in actual_names)
    # assert ('Radio Super Latina La Merced' in actual_names)
    # assert ('RADIO LA FUERTE' in actual_names)
