#####
# This is only to troubleshoot why things fail on travis-ci servers that do
# not fail on my own test environment.
#####

Feature: Troubleshoot

  Scenario: Tshoot 1
    Given there are no lingering output files
    And individual recordings are present in the default input place
    Then ls
#    And fail

    Given there are no lingering output files
    And individual recordings are present in the default input place
    When tshoot
    Then ls
