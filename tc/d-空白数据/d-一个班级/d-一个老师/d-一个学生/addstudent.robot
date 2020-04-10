*** Settings ***
Resource  rflib/studentdata.robot
Library  pylib.SchoolStudentLib.Student
Library  pylib.SchoolClassLib.Grade

*** Test Cases ***
添加不同登录名的学生-tc002002
    ${ret}  add a student  ${username_2}  ${realname}  ${gradeId}
    should be true  $ret['retcode'] == 0
    ${id}  evaluate  $ret['id']
    ${id_bool}  verify student  ${id}
    should be true  $id_bool
    [Teardown]  delete student  ${id}

删除学生-tc002081
    ${id}  get student id
    ${ret}  delete student  ${id}
    should be true  $ret['retcode'] == 0
    ${id_bool}  verify student  ${id}
    should be true  not $id_bool
    [Teardown]  add a student  ${username}  ${realname}  ${gradeId}