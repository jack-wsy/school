# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/30
# @file : UiBase
# @version : 1.0.0
# @desc :  Web UI Base
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pylib.constant import *

class UiBase:

    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = HOST

    def __open(self,url):
        self.driver.get(self.base_url+url)

    def open(self):
        self.__open(self.uri)

    def find_element(self,*location):
        return self.driver.find_element(*location)

    def find_elements(self,*location):
        return self.driver.find_elements(*location)

    def is_element(self,*location):
        try:
            eles = WebDriverWait(self.driver,3).until(expected_conditions.presence_of_element_located(location))
            if eles:
                return True
        except:
            return False