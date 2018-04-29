# Created by philip at 4/24/18
Feature: Retreive thumbnail images from an arbitrary path to assist in figuring
  out what I have.

  #These are more like unit testcases but for while I'm getting a feel for BDD I think
  # it's OK to start with this kind of stuff.
  Scenario: Retrieve thumbnails for hardcoded non-recursive path
    When Everything is set up in tests/testbed/recordings
    Then I get an HTML file allowing me to view all thumbnails in tests/testbed/recordings

  Scenario: Retrieve thumbnails for hardcoded recursive path
    When Everything is set up in tests/testbed/recordings and subdirs
    Then I get an HTML file allowing me to view all thumbnails in tests/testbed/recordings and subdirs

  Scenario: Retrieve thumbnails for arbitrary recursive path
    When I pass in the name tests/testbed/another-path
    And Everything is set up in tests/testbed/another-path and subdirs
    Then I get an HTML file allowing me to view all thumbnails in tests/testbed/another-path and subdirs
