*** Settings ***
Library  pylib.SchoolStudentLib.Student
Library  pylib.SchoolClassLib.Grade
Resource  rflib/studentdata.robot

*** Test Cases ***
添加学生-tc002001
    ${list_ret}  get grade
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${classId}  evaluate  $list_ret['id']
    ${phonenumber}  create phone  0
    ${ret}  add student  ${username}  ${realname}  ${gradeId}  ${classId}  ${phonenumber}
    ${id}  evaluate  $ret['id']
    should be true  $ret['retcode'] == 0
    ${list_ret}  get student
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    should be true  $id == $list_ret['id']
    [Teardown]  delete student  ${id}
