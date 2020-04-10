*** Settings ***
Library  pylib.SchoolTeacherLib.Teacher
Resource  rflib/teacherdata.robot

*** Test Cases ***
添加不同登录名的老师-tc001002
    ${ret}  add a teacher  ${username_2}  ${realname}  ${ms_sports}
    should be true  $ret['retcode'] == 0
    ${id}  evaluate  $ret['id']
    ${list_ret}  get teacher  ${ms_sports}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    should be true  $id == $list_ret['id']
    [Teardown]  delete teacher  ${id}

添加相同登录名的老师-tc001003
    ${ret}  add a teacher  ${username}  ${realname}  ${ms_english}
    should be true  $ret['retcode'] == 1
    ${sum}  sum loginname    ${username}
    should be true  $sum == 1

对不存在的老师进行修改-tc001051
    ${ret}  modify teacher  ${not_exist_teacherId}  realname=${realname_modify}
    should be true  $ret['retcode'] == 1

