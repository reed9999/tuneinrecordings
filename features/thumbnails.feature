#####
# Created by philip at 4/24/18
# BDD aspects of the project are arguably contrived to get me thinking in
# BDD terms. In a larger project, many of these "features" would be unit
# tests with the features being coarser and less implementation-coupled.
# At least that is my reading of BDD.
#####

@fixture.app
Feature: Retrieve thumbnail images from an arbitrary path to assist in figuring
  out what I have.

  #These are more like unit testcases but for while I'm getting a feel for BDD I think
  # it's OK to start with this kind of stuff.

#  Scenario: Retrieve thumbnails for hardcoded non-recursive path
#Who cares? It wasn't any harder to implement the recursive one.

  Scenario: Retrieve thumbnails for hardcoded recursive path
    If everything is in a default place, we get a nice tidy HTML file.
    NOTE 1: The HTML file is not that tidy yet. Add some criteria for what I want.
    NOTE 2: It's weird that the test dir should be the default. Really needs a better default.
    Although in fairness it could be ".", the current dir, whatever.

    Given there are no lingering output files
    And individual recordings are present in the default input place
    When I run the app
    Then I get an HTML output file in the default output place
    And the output file displays images for img tags in the default place and subdirs
#    HARDER TO IMPLEMENT:
#    And the output file gives directory locations for images displayed
#    And the images have alt tags for all alt tags in the default place and subdirs.

  Scenario: Retrieve thumbnails for hardcoded recursive path storing in arbitrary output file
    As above, but it should work even if the output file isn't the default place.

    Given there are no lingering output files
    And individual recordings are present in the default input place
    When I run the app
    Then I get an HTML output file in an arbitrary output place
    And the output file displays images for img tags in the default place and subdirs
    And the images have alt tags for all alt tags in the default place and subdirs.

  Scenario: Retrieve thumbnails for arbitrary recursive path
    As above, but it should also work even if the input files aren't in the default place.

    Given there are no lingering output files
    And individual recordings are present in an arbitrary input place
    When I run the app
    Then I get an HTML output file in an arbitrary output place
    And the output file displays images for img tags in the arbitrary place and subdirs
    And the images have alt tags for all alt tags in abitrary place and subdirs.

  Scenario: Use the GUI to assign names to images
    The GUI doesn't yet exist so expecting it to do something is absurd.

    Given the GUI is running
    When I invoke the image naming dialogue
    And I use the GUI to assign names to images
    Then the names I assigned are retained.