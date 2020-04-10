*** Settings ***
Library  pylib.SchoolClassLib.Grade
Resource  rflib/gradedata.robot

*** Test Cases ***
修改班级名-tc000051
    ${list_ret}  get grade  ${grade}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${id}  evaluate  $list_ret['id']
    ${ret}  modify grade  ${id}  ${className_modify}  ${studentLimit}
    should be true  $ret['retcode'] == 0
    ${modify_bool}  is grade exist  ${grade}  className=${className_modify}
    should be true  ${modify_bool}
    [Teardown]  modify grade  ${id}  ${className}  ${studentLimit}

修改为同名班级-tc000052
    ${list_ret}  get grade  ${grade}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${id}  evaluate  $list_ret['id']
    ${ret}  modify grade  ${id}  ${className_2}  ${studentLimit_100}
    should be true  $ret['retcode'] == 10000
    ${modify_bool}  is grade exist  ${grade}  className=${className}
    should be true  ${modify_bool}
    ${modify_bool}  is grade exist  ${grade}  studentLimit=${studentLimit_100}
    should be true  not $modify_bool

修改班级时使用不存在的Id-tc000053
    ${ret}  modify grade  ${not_exist_id}  ${className}   ${studentLimit_100}
    should be true     $ret['retcode']==404