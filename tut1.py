

from selenium import webdriver

# webdriver are basically used to provide you access to website so that you make 
# actions to webiste like clicking any button or other oprations
# path of webdriver 
path = '/home/sahib/selenium-tut/chromedriver'

driver = webdriver.Chrome(path)


driver.get('https://www.techwithtim.net')


# # to loacte the search bar
search_bar = driver.find_element_by_name("s")

# # to get title of your webpage
# print(driver.title)

# https://selenium-python.readthedocs.io/locating-elements.html

# to close the current tab
# driver.close()

# to close complete browser
# driver.quit()