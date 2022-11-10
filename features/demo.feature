Feature: showing off behave

  Scenario Outline: run a simple test
    Given <url> name
    When Find <element> on page
#    And  Fill <data> in element
#    And  Press button on <element>
#    Then Check that element Equal to <something>

    Examples:
      | url      | element         | data         | something       |
      | https://www.wikipedia.org/ | search_field | data_1 | body   |
      |"https://www.wikipedia.org/ | search_field | data_2 | expected_result |