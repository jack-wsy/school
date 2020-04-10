*** Settings ***
Library  pylib.SchoolClassLib.Grade
Library  pylib.SchoolTeacherLib.Teacher

*** Variables ***
${ms_math}  1
${ms_science}  5
${ms_english}  11
${ms_sports}  12
${hs_chinese}  13
${hs_math}  14
${username}  teacher
${username_2}  teacher_2
${realname}  测试添加老师
${realname_modify}  测试修改老师
${email}   jcy@123.com
${not_exist_teacherId}  10000



*** Keywords ***
add a teacher
    [Arguments]  ${username}  ${realname}  ${subjectId}
    ${phonenumber}  create phone or idcard  0
    ${idcardnumber}  create phone or idcard  1
    ${list_ret}  get grade
    ${list_ret}  evaluate  $list_ret['retlist'][0]
    ${id}  evaluate  $list_ret['id']
    ${ret}  add teacher  ${username}  ${realname}  ${subjectId}  ${phonenumber}  ${email}  ${idcardnumber}  ${id}
    [Return]  ${ret}