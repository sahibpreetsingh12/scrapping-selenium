
# we can access any element on webpage using class, Name, ID and Tags
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# keys import provide us facility like Enter or Escape key so that we can interact with our 
# search bar for this tutorial
from selenium.webdriver.common.keys import Keys
path = '/home/sahib/selenium-tut/chromedriver'

driver = webdriver.Chrome(path)

driver.get('https://www.techwithtim.net/')

# to get access to serach bar 
search_bar = driver.find_element_by_name("s")

# it is recommended to clear before sending keys
search_bar.clear()

# send our keys ( what we want to search in this case)
search_bar.send_keys("test")

# see what we have searched
res = search_bar.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # name of the tag you are looking
    articles = main.find_elements_by_tag_name("article")
    for i,art in enumerate(articles):
        head = art.find_element_by_class_name("entry-summary")
        print(i,head.text,'\n')

finally:
    driver.quit()

