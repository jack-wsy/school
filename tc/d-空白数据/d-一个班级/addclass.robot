*** Settings ***
Resource  rflib/gradedata.robot
Library  pylib.SchoolClassLib.Grade

*** Test Cases ***
添加不同年级的同名课程-tc000002
    ${ret}  add grade   ${grade_2}  ${className}    ${studentLimit}
    ${id}  evaluate  $ret['id']
    ${invitecode}  evaluate  $ret['invitecode']
    should be true  $ret['retcode'] == 0
    ${id_exist}  is grade exist  ${grade_2}  id=${id}
    ${invitecode_exist}  is grade exist  ${grade_2}  invitecode=${invitecode}
    should be true  ${id_exist}
    should be true  ${invitecode_exist}
    [Teardown]  delete grade  ${id}

添加同年级同名课程-tc000003
    ${ret}  add grade  ${grade}  ${className}  ${studentLimit}
    should be true  $ret['retcode'] == 1
    ${sum}  sum_grade  ${grade}   ${className}
    should be true   $sum == 1

