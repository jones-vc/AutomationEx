from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

# set the path to the webdriver executables
gecko_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\geckodriver.exe"
chrome_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\chromedriver.exe"

# to keep chrome and chromedriver open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# create a webdriver instance (chrome)
driver = webdriver.Chrome(chrome_options=chrome_options)

# go to webpage
driver.get("https://satrngselcypr.z16.web.core.windows.net/")

# find the logout button by css selector and click it
btn_logout = driver.find_element(By.CSS_SELECTOR,"#logout").click()

# find the dropdown, select the checkbox, select "French"
dd_language = driver.find_element(By.CSS_SELECTOR, "#login > table > tbody > tr:nth-child(3) > td:nth-child(2) > select")
cbx_languages = Select(dd_language)
cbx_languages.select_by_visible_text("French")

# find the username field and enter "admin"
fld_username = driver.find_element(By.CSS_SELECTOR, "#username").send_keys("admin")

# find the password field, clear it first and enter "superduper"
fld_password = driver.find_element(By.CSS_SELECTOR,"#password")
fld_password.clear
fld_password.send_keys("superduper")

# find and click the login button
btn_login = driver.find_element(By.CSS_SELECTOR, "#login > table > tbody > tr:nth-child(4) > td:nth-child(2) > span > label").click()

# quit driver
driver.quit()
