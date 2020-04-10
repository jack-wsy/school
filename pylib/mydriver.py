# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# @author : Wsy
# @date : 2019/9/30
# @file : mydriver
# @version : 1.0.0
# @desc :  driver object

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def browser():

    driver = webdriver.Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    # driver = webdriver.PhantomJS()
    return driver
