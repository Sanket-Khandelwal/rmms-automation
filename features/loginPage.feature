# Created by sanket.khandelwal at 8/10/2024
Feature: Login functionality for RMMS application
  # Enter feature description here

  Scenario: Valid username and password
    Given open browser
    When enter username and password
    Then verify auth page