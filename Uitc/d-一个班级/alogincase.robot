*** Settings ***
Library  case/tc005001.py  WITH NAME  tc005001
Library  case/tc005081.py   WITH NAME  tc005081

*** Test Cases ***
1
    [Setup]  tc005001.setUp
    tc005001.steps  admin
    [Teardown]  tc005001.tearDown

2
    [Setup]  tc005081.setUp
    tc005081.steps
    [Teardown]  tc005081.tearDown