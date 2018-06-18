"""
This is the variables exercise in Selenium
"""

# Open Selenium with Firefox Browser
from selenium import webdriver

my_first_selenium_script =  webdriver.Firefox()

my_first_selenium_script.get("www.testdemy.com")

my_first_selenium_script.quit()