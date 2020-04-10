*** Settings ***
Library  pylib.SchoolTeacherLib.Teacher
Resource  rflib/teacherdata.robot
Suite Setup  add a teacher  ${username}  ${realname}  ${ms_math}