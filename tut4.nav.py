from selenium import webdriver


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# keys import provide us facility like Enter or Escape key so that we can interact with our 
# search bar for this tutorial
from selenium.webdriver.common.keys import Keys

path = '/home/sahib/selenium-tut/chromedriver'

driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net")

# Link Text basically your anchor tag Info
link = driver.find_element_by_link_text("Python Programming")

# to click on that link
link.click()

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    main.click()

    # click on arted get stButton
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    main.click()

    for i in range(3):
      # to get back pages from cache memory we acquired
        driver.back()
except:
    driver.quit()


