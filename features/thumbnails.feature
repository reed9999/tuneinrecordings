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
    And Individual recordings are present in tests/testbed-working/recordings
    When I run the app
#    Then I get an HTML file tests/output/thumbnails.html allowing me to view all thumbnails in tests/testbed-working/recordings
    Then I get an HTML file ./thumbnails.html with img and alt for all thumbnails in tests/testbed-working/recordings.


  Scenario: Retrieve thumbnails for hardcoded recursive path
    Given There are no lingering output files
    And Subdirs with recordings are present in tests/testbed-working/recordings
    When I run the app
    Then I get an HTML file ./thumbnails.html with img and alt for all thumbnails in tests/testbed-working/recordings and subdirs

  @fixture.app
  Scenario: Retrieve thumbnails for hardcoded recursive path storing in arbitrary output file
    Given There are no lingering output files
    And Subdirs with recordings are present in tests/testbed-working/recordings
    When I run the app with output file ./recordings/output/thumbnails.html
    #Really something like this should be default anyway.
    Then I get an HTML file ./recordings/output/thumbnails.html with img and alt for all thumbnails in tests/testbed-working/recordings and subdirs

  Scenario: Retrieve thumbnails for arbitrary recursive path
    Given There are no lingering output files
    And Subdirs with recordings are present in tests/testbed/another-path
    When I run the app passing in the name tests/testbed/another-path
    Then I get an HTML file ./thumbnails.html allowing me to view all thumbnails in tests/testbed/another-path and subdirs
#    Then I get an HTML file tests/output/thumbnails.html with relative paths allowing me to view all thumbnails including subdirs.

  Scenario: Use the GUI to assign names to images
    Given the GUI is running
    When I invoke the image naming dialogue
    And I use the GUI to assign names to images
    Then the names I assigned are retained.