from selenium import webdriver


import time

# keys import provide us facility like Enter or Escape key so that we can interact with our 
# search bar for this tutorial
from selenium.webdriver.common.keys import Keys

path = '/home/sahib/selenium-tut/chromedriver'

driver = webdriver.Chrome(path)

driver.get('https://www.youtube.com/')

# to get access to serach bar of you tube
search_bar = driver.find_element_by_id("search")


# send our keys ( what we want to search in this case)
search_bar.send_keys("Indian Test")

# see what we have searched
search_bar.send_keys(Keys.RETURN)


# stop screen for 10 seconds
time.sleep(10)

driver.quit()