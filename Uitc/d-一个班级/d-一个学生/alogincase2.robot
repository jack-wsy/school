*** Settings ***
Library  case/tc005002.py  WITH NAME   tc005002

*** Test Cases ***
3
    [Setup]  tc005002.setUp
    tc005002.steps
    [Teardown]  tc005002.tearDown