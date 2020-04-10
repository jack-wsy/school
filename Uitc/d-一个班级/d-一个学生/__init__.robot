*** Settings ***
Library  pylib.SchoolStudentLib.Student
Resource  rflib/studentdata.robot
Suite Setup  add a student  ${username}  ${realname}  ${gradeId}