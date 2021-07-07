

from selenium import webdriver
import pandas as pd
import xlsxwriter
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# keys import provide us facility like Enter or Escape key so that we can interact with our 
# search bar for this tutorial
from selenium.webdriver.common.keys import Keys

# to counter exception
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})


# read original unique questions 
file_original = pd.read_csv('/home/sahib/New-question.csv')
sentences = list(file_original['question'].values[:2])

workbook = xlsxwriter.Workbook('/home/sahib/nlu-file.xlsx')

# By default worksheet names in the spreadsheet will be 
# Sheet1, Sheet2 etc., but we can also specify a name.
worksheet = workbook.add_worksheet("sheet1")


worksheet.write('A1', 'Original-question')
worksheet.write('B1', 'Paraphrased-question')

path = '/home/sahib/selenium-tut/chromedriver'


driver = webdriver.Chrome(path, options= option)

driver.get('https://quillbot.com/')


# sentences = ["how many langugaes present in IDP","In india we have 29 states","whos going IDP do they have indicators"]

# list containing all lists of variations
scores = []


for k,sent in enumerate(sentences):

	for_each_sent = []

	# to get access to input box of quilbot
	search_bar = driver.find_element_by_id("inputText")

	# make sure your input text field is clear at first
	search_bar.clear()
	

	# send our keys ( what we want to search in this case)
	search_bar.send_keys(sent)
	

	# see what we have typed
	search_bar.send_keys(Keys.RETURN)
	time.sleep(3)


	# rephrased_list = []


	if k==0:
	# finding the button using class name for paraphrasing first time
		button = driver.find_element_by_class_name('false')
		print("yes")
	else:
		
		# when we click the Rephrase button in loop after first time
		button = driver.find_element_by_class_name('jss209')
		print("yes",k)


	# clicking on the button first time
	button.click()

	
	# wait for 8 seconds
	time.sleep(8)

	#first rephrased text on right side of quilbot
	rephrase = driver.find_element_by_id('editable-content-within-article')

	first_occ_text = rephrase.text

	if first_occ_text != rephrase.text:
		print(f"storing first mapping of sentence  {k}")

	  # check if rephrased sentence is same as original sentence

		scores.append([first_occ_text,rephrase.text])
		for_each_sent.append(first_occ_text)

	time.sleep(8)

	# now after genrating paraphrase for first time for a question 
	# we will now make 2 retrievls of it
	for i in range(5):

		try:

			# hitting rephrase  button again
			rephrase_button = driver.find_element_by_class_name('jss209')
			button.click()
			time.sleep(8)
			rephrase = driver.find_element_by_id('editable-content-within-article')

			# nth rephrased sentences
			n_rephrased_sent = rephrase.text

			 # check if rephrased sentence is same as original sentence	 and n_rephrased_sent is not already present
			if (first_occ_text != n_rephrased_sent) and (n_rephrased_sent not in for_each_sent) : 

				scores.append([first_occ_text,rephrase.text])


		except :
			# driver.switch_to.window(handles[0])# first window

			# cancel_way = driver.find_element_by_class_name('MuiDialog-container MuiDialog-scrollPaper')
			# # MuiPaper-root MuiDialog-paper jss73 MuiDialog-paperScrollPaper MuiDialog-paperWidthMd MuiPaper-rounded

			# cancel_way.click()

			# print("clicked outside")

			driver.refresh()
			

			print(f"when error occured for sentence {k}")

			k=0
			# to get access to input box of quilbot
			search_bar = driver.find_element_by_id("inputText")

			# make sure your input text field is clear at first
			search_bar.clear()
			time.sleep(6)

			# send our keys ( what we want to search in this case)
			search_bar.send_keys(sent)
			# time.sleep(6)

			# see what we have typed
			search_bar.send_keys(Keys.RETURN)


			# now page has refreshed click on Paraphrase button
			button = driver.find_element_by_class_name('false')


			# clicking on the button first time
			button.click()
			# wait for 8 seconds
			time.sleep(8)

			#first rephrased text on right side of quilbot
			rephrase = driver.find_element_by_id('editable-content-within-article')
			first_occ_text = rephrase.text

			if first_occ_text != rephrase.text:  # check if rephrased sentence is same as original sentence
				scores.append([first_occ_text,rephrase.text])



			# rephrase_button = driver.find_element_by_class_name('jss209')
			# button.click()
			# time.sleep(8)
			# rephrase = driver.find_element_by_id('editable-content-within-article')

			# if first_occ_text != rephrase.text:  # check if rephrased sentence is same as original sentence
			# 	scores.append([first_occ_text,rephrase.text])


			# cancel = driver.find_element_by_class_name('MuiIconButton-label')
			# cancel.click()
		# finally:
		# 	handles = driver.window_handles
		# 	size = len(handles)

		# 	print(f"FInally handles {handles} and size is now {size} ")

			


print(scores)


# Start from the first cell. Rows and
# columns are zero indexed.
row = 1
col = 0
  
# Iterate over the data and write it out row by row.
for name, score in (scores):
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, score)
    row += 1


	
workbook.close()
# Some data we want to write to the worksheet.

driver.quit()



