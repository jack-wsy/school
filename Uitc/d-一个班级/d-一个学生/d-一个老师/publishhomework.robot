*** Settings ***
Library  case/tc005101.py  WITH NAME  tc005101
Resource  rflib/studentdata.robot
Resource  rflib/teacherdata.robot

*** Test Cases ***
4
    [Setup]  tc005101.setUp
    tc005101.steps  teacher  studentlogin
    [Teardown]  tc005101.tearDown