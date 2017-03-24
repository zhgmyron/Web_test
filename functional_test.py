# -*- coding: UTF-8 -*-
from selenium import webdriver
driver = webdriver.Chrome("F:\soft\chromedriver.exe")
driver.get('http://localhost:8000')
assert 'Django' in driver.title
