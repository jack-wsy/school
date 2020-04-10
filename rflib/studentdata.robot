*** Settings ***
Library  pylib.SchoolClassLib.Grade
Library  pylib.SchoolStudentLib.Student

*** Variables ***
${username}  studentlogin
${username_2}  studentlogin2
${realname}  测试添加学生
${gradeId}  1

*** Keywords ***
add a student
    [Arguments]  ${username}  ${realname}  ${gradeId}
    ${list_ret}  get grade
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${classId}  evaluate  $list_ret['id']
    ${phonenumber}  create phone  0
    ${ret}  add student  ${username}  ${realname}  ${gradeId}  ${classId}  ${phonenumber}
    [Return]   ${ret}