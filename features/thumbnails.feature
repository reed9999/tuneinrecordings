#####
# Created by philip at 4/24/18
# BDD aspects of the project are arguably contrived to get me thinking in
# BDD terms. In a larger project, many of these "features" would be unit
# tests with the features being coarser and less implementation-coupled.
# At least that is my reading of BDD.
#####

@fixture.app #Doesn't seem to be read
Feature: Retrieve thumbnail images from an arbitrary path to assist in figuring
  out what I have.

  #These are more like unit testcases but for while I'm getting a feel for BDD I think
  # it's OK to start with this kind of stuff.

  @fixture.app
  Scenario: Retrieve thumbnails for hardcoded non-recursive path
    Given There are no lingering output files
    And Individual recordings are present in tests/testbed/recordings
    When I run the app
#    Then I get an HTML file tests/output/thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings
    Then I get an HTML file ./thumbnails.html with img and alt for all thumbnails in tests/testbed/recordings

  Scenario: Same as above but the dot at the end makes it fail which makes no sense
    Given There are no lingering output files
    And Individual recordings are present in tests/testbed/recordings
    When I run the app
#    Then I get an HTML file tests/output/thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings
    Then I get an HTML file ./thumbnails.html with img and alt for all thumbnails in tests/testbed/recordings.

  Scenario: Retrieve thumbnails for hardcoded recursive path
    Given There are no lingering output files
    And Subdirs with recordings are present in tests/testbed/recordings
    When I run the app
    Then I get an HTML file tests/output/thumbnails.html allowing me to view all thumbnails in tests/testbed/recordings and subdirs
#    Then I get an HTML file tests/output/thumbnails.html with relative paths allowing me to view all thumbnails including subdirs.

  Scenario: Retrieve thumbnails for arbitrary recursive path
    Given There are no lingering output files
    And Subdirs with recordings are present in tests/testbed/another-path
    When I run the app passing in the name tests/testbed/another-path
    Then I get an HTML file ./thumbnails.html allowing me to view all thumbnails in tests/testbed/another-path and subdirs
#    Then I get an HTML file tests/output/thumbnails.html with relative paths allowing me to view all thumbnails including subdirs.

  @fixture.app
  Scenario: Using the fixture
    This scenario is not even coupled with app implementation--it's test implementation!
    Really it's just a fun way for me to track that I want to learn to get behave fixtures
    working!

    When I run a test with a fixture
    Then The test should use the fixture.