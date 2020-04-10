# -*- coding:utf-8 -*-
# !/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/28
# @file : SchoolClassLib
# @version : 1.0.0
# @desc :  School Grade Lib
import pprint

import requests
from pylib.Base import Base

class Grade(Base):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    # 获取班级列表
    def get_grade(self,gradeid = None, action = "list_classes_by_schoolgrade" ):
        result = requests.get(self.get_grade_address(),params={
            "vcode" : self.get_vcode(),
            "action" : action,
            "gradeid" : gradeid
        }).json()

        return result

    # 添加班级
    def add_grade(self,grade,name,studentlimit,action = "add"):
        result = requests.post(self.get_grade_address(),data={
            "vcode" : self.get_vcode(),
            "action" : action,
            "grade" : grade,
            "name" : name,
            "studentlimit" : studentlimit
        }).json()

        return result

    # 修改班级
    def modify_grade(self,classId,name,studentlimit,action = "modify"):
        result = requests.put(self.get_grade_address() + "/" + str(classId),data={
            "vcode" : self.get_vcode(),
            "action" : action,
            "name" : name,
            "studentlimit" : studentlimit
        }).json()

        return result

    # 删除班级
    def delete_grade(self,classId):
        result = requests.delete(self.get_grade_address() + "/" + str(classId) ,data={
            "vcode" : self.get_vcode()
        }).json()

        return result

    # 删除所有班级
    def delete_grade_all(self):
        result = self.get_grade()["retlist"]
        for one in result:
            requests.delete(self.get_grade_address() + "/" + str(one["id"]),data={
                "vcode" : self.get_vcode()
            })
        again_result = self.get_grade()["retlist"]
        if again_result:
            raise Exception("classes are not empty")

    # 遍历列表内容
    def is_grade_exist(self,gradeId,*,id = None,invitecode = None,className = None,studentLimit = None):
        result = self.get_grade(gradeId)["retlist"]
        for one in result:
            if id and one["id"] == int(id):
                return True
            if invitecode and one["invitecode"] == invitecode:
                return True
            if className and one["name"] == className:
                return True
            if studentLimit and one["studentlimit"] == studentLimit:
                return True
        return False

    # 统计同年级是否有重名班级
    def sum_grade(self,gradeId,className):
        sum = 0
        result = self.get_grade(gradeId)["retlist"]
        for one in result:
            if one["name"] == className:
                sum += 1
        return sum

    def get_grade_id(self):
        result = self.get_grade()
        gradeId = result['retlist'][0]['id']
        return gradeId


if "__main__" == __name__:
    g = Grade()
    # pprint.pprint(g.add_grade("1","测试一班","80"))
    # pprint.pprint(g.add_grade("1", "测试二班", "80"))
    # pprint.pprint(g.modify_grade(231232,"实验二班","60"))
    # pprint.pprint(g.delete_grade(231640))
    pprint.pprint(g.get_grade(),indent=2)
    # g.delete_grade_all()
    # pprint.pprint(g.is_grade_exist("2",className="测试二班_修改"))
    # print(b"\xe6\xb5\x8b\xe8\xaf\x95\xe4\xb8\x80\xe7\x8f\xad-703-1".decode('utf8'))