*** Settings ***
Library  pylib.SchoolTeacherLib.Teacher
Resource  rflib/teacherdata.robot

*** Test Cases ***
修改老师信息-tc001052
    ${list_ret}  get teacher  ${ms_math}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${teacherId}  evaluate  $list_ret['id']
    ${list_ret}  get grade
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${gradeId_1}  evaluate  $list_ret['id']
    ${list_ret}  get grade
    ${list_ret}  evaluate  $list_ret['retlist'][1]
    ${gradeId_2}  evaluate  $list_ret['id']
    ${ret}  modify teacher  ${teacherId}  ${gradeId_1}  ${gradeId_2}  realname=${realname_modify}  subjectid=${ms_math}
    should be true  $ret['retcode'] == 0
    ${list_ret}  get teacher  ${ms_math}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${teachercalsslist}  evaluate  $list_ret['teachclasslist']
    ${get_realname}  evaluate  $list_ret['realname']
    should be true  $teachercalsslist == [$gradeId_1,$gradeId_2]
    should be true  $get_realname == $realname_modify
    [Teardown]  modify teacher  ${teacherId}  ${gradeId_1}  realname=${realname}  subjectid=${ms_math}
