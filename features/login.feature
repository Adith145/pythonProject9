Feature:Validate the amazon mobile search


  Scenario: find the  oneplus mobile less than 30000
    Given launch the chrome browser
    When  search the mobile less than 30000 oneplus mobile
    And   click on sort by option and select newest arrivals search
    Then i will redirect to home page verify the title
