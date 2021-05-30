

from selenium import webdriver

# webdriver are basically used to provide you access to website so that you make 
# actions to webiste like clicking any button or other oprations
# path of webdriver 
path = '/home/sahib/selenium-tut/chromedriver'

driver = webdriver.Chrome(path)

driver.get('https://www.youtube.com/')