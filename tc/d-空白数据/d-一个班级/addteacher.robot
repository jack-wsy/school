*** Settings ***
Library  pylib.SchoolTeacherLib.Teacher
Library  pylib.SchoolClassLib.Grade
Resource  rflib/teacherdata.robot

*** Test Cases ***
添加初中数学老师-tc001001
#    ${phonenumber}  create phone or idcard  0
#    ${idcardnumber}  create phone or idcard  1
#    ${list_ret}  get grade
#    ${list_ret}  evaluate  $list_ret['retlist'][0]
#    ${id}  evaluate  $list_ret['id']
#    ${ret}  add teacher  ${username}  ${realname}  ${ms_math}  ${phonenumber}  ${email}  ${idcardnumber}  ${id}
    ${ret}  add a teacher  ${username}  ${realname}  ${ms_math}
    ${teacherId}  evaluate  $ret['id']
    ${list_ret}  get teacher  ${ms_math}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    should be true  $teacherId == $list_ret['id']
    [Teardown]  delete teacher  ${teacherId}

