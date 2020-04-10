*** Settings ***
Library  pylib.SchoolClassLib.Grade
Resource  rflib/gradedata.robot

*** Test Cases ***
删除不存在的课程
    ${ret}  delete grade  ${not_exist_id}
    should be true  $ret['retcode'] == 404

删除课程
    ${list_ret}  get grade  ${grade}
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${id}  evaluate  $list_ret['id']
    ${ret}  delete grade  ${id}
    should be true  $ret['retcode'] == 0
    ${id_bool}  is grade exist  ${grade}  id=${id}
    should be true  not $id_bool
    [Teardown]  add grade  ${grade}  ${className}  ${studentLimit}