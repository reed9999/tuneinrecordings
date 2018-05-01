# Created by philip at 4/24/18

@fixture.app
Feature: Retrieve thumbnail images from an arbitrary path to assist in figuring
  out what I have.

  #These are more like unit testcases but for while I'm getting a feel for BDD I think
  # it's OK to start with this kind of stuff.
  Scenario: Retrieve thumbnails for hardcoded non-recursive path
    Given There are no lingering output files
    And Everything is set up in tests/testbed/recordings
    When I run the app
#    Then I get an HTML file tests/output/thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings
    Then I get an HTML file ./thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings

  Scenario: Retrieve thumbnails for hardcoded recursive path
    Given There are no lingering output files
    And Everything is set up in tests/testbed/another-path and subdirs
    When I run the app
    Then I get an HTML file tests/output/thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings and subdirs

  Scenario: Retrieve thumbnails for arbitrary recursive path
    Given There are no lingering output files
    And Everything is set up in tests/testbed/another-path and subdirs
    When I run the app passing in the name tests/testbed/another-path
    Then I get an HTML file ./thumbnails.html allowing me to view all thumbnails in tests/testbed/another-path and subdirs
#    Then I get an HTML file tests/output/thumbnails.html with relative paths allowing me to view all thumbnails in tests/testbed/another-path and subdirs
