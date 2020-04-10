# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/28
# @file : Base
# @version : 1.0.0
# @desc :  基础类
from random import randint

from pylib.constant import *

class Base:
    def __init__(self):
        self.__address = HOST
        self.__gradeUri = GRADE
        self.__teacherUri = TEACHER
        self.__studentUri = STUDENT
        self.__vcode = VCODE

    def get_grade_address(self):
        return self.__address + self.__gradeUri

    def get_teacher_address(self):
        return self.__address + self.__teacherUri

    def get_student_address(self):
        return self.__address + self.__studentUri

    def get_vcode(self):
        return self.__vcode




