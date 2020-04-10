*** Settings ***
Library  pylib.SchoolClassLib.Grade
Library  pylib.SchoolStudentLib.Student
Library  pylib.SchoolTeacherLib.Teacher
Resource  rflib/gradedata.robot
Suite Setup  run keywords  delete student all  AND  delete teacher all  AND  delete grade all
...  AND  add grade  ${grade}  ${className}  ${studentLimit}
Suite Teardown  run keywords   delete student all  AND  delete teacher all  AND  delete grade all