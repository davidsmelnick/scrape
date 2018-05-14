from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.google.com')

search_bar = driver.find_element_by_id('lst-ib')
search_bar.send_keys('lucky')
search_button = driver.find_element_by_name('btnK')
search_button.click()