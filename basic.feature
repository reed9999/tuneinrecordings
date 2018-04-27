# Created by philip at 4/24/18
Feature: Basic functionality of whatever intersectional queries I want to make of TuneIn
  Everything should go here for now, because I don't think this utility will be very complex.

  Scenario: Retrieve simple language/genre pair (music)
    When I pass in a language and music genre
    Then I get a convenient list of all stations matching both language and genre

  Scenario: Retrieve simple country list
    When I pass in the country Peru
    Then I get a convenient list of all stations from Peru
