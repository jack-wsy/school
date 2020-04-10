*** Settings ***
Library  pylib.SchoolClassLib.Grade
Resource  rflib/gradedata.robot
Suite Setup  add grade  ${grade}    ${className}    ${studentLimit}