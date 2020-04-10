*** Settings ***
Library  pylib.SchoolClassLib.Grade
Resource  rflib/gradedata.robot

*** Test Cases ***
添加班级-tc000001
    ${ret}  add grade   ${grade}    ${className}    ${studentLimit}
    should be true  $ret['retcode']==0
    ${list_ret}     get grade  ${grade}
    ${list_ret}     evaluate  $list_ret['retlist'][0]
    should be true  $list_ret['id'] == $ret['id']
    should be true  $list_ret['invitecode'] == $ret['invitecode']
    [Teardown]  delete grade all