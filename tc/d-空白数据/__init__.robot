*** Settings ***
Library  pylib.SchoolClassLib.Grade
Library  pylib.SchoolStudentLib.Student
Library  pylib.SchoolTeacherLib.Teacher
Suite Setup  run keywords  delete student all  AND  delete teacher all  AND  delete grade all
Suite Teardown  run keywords   delete student all  AND  delete teacher all  AND  delete grade all