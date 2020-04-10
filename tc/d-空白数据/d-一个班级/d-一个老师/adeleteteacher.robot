*** Settings ***
Library  pylib.SchoolTeacherLib.Teacher
Resource  rflib/teacherdata.robot

*** Test Cases ***
删除不存在的老师-tc001081
    ${ret}  delete teacher  ${not_exist_teacherId}
    should be true  $ret['retcode'] == 404

删除老师-tc001082
    ${list_ret}  get teacher  ${ms_math}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${teacherId}  evaluate  $list_ret['id']
    ${ret}  delete teacher  ${teacherId}
    should be true  $ret['retcode'] == 0
    ${sum}  sum loginname  ${username}
    should be true  $sum == 0
    [Teardown]  add a teacher  ${username}  ${realname}  ${ms_math}